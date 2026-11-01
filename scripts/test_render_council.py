import contextlib
import io
from pathlib import Path
import tempfile
import unittest

from render_council import InvalidSource, main, render

CUTOFF = '2026-11-01T14:50:00+08:00'


class CouncilTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'members').mkdir()
        self.person('one', '000001', 'one')

    def person(self, filename, member_id, github, name='同名成員'):
        (self.root / f'members/{filename}.md').write_text(
            f'# {name}\nMember ID：{member_id}\nGitHub：{github}\n', encoding='utf-8')

    def record(self, role='活動', person='one', state='已生效', cutoff=CUTOFF,
               effective='2026-10-01T00:00:00+08:00'):
        values = {
            '人員': f'[成員]({person}.md)',
            '決定依據': '[原案](https://example.com/decision)',
            '本人接受': '[接受](https://example.com/acceptance)',
            '生效條件': '原案條件已核對', '生效時間': effective,
            '核對截止': cutoff, '本次核對': '[核對](https://example.com/review)',
            '核對結果': state, '尚未完成': '無',
        }
        return f'## {role}\n### Leader\n' + ''.join(f'- {k}：{v}\n' for k, v in values.items())

    def source(self, *records):
        (self.root / 'members/r-and-r-assignment.md').write_text(
            f'# 分工\nCouncil 核對截止：{CUTOFF}\n' + '\n'.join(records), encoding='utf-8')

    def run_cli(self, *args):
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return main(['--root', str(self.root), *args])

    def active_section(self):
        return render(self.root).split('## 截至核對時間可確認的 Council')[1].split('## 尚未生效的安排')[0]

    def test_two_roles_one_person(self):
        self.source(self.record('活動'), self.record('網域'))
        section = self.active_section()
        self.assertEqual(section.count('[同名成員](one.md)'), 1)
        self.assertIn('活動<br>網域', section)

    def test_last_role_ended_removes_person(self):
        self.source(self.record(state='已終止'))
        self.assertNotIn('[同名成員]', self.active_section())
        self.assertIn('截至核對時間未有有效 Council', render(self.root))

    def test_one_ended_role_preserves_other(self):
        self.source(self.record('活動', state='已終止'), self.record('網域'))
        section = self.active_section()
        self.assertIn('[同名成員]', section)
        self.assertNotIn('活動', section)

    def test_same_name_different_people(self):
        self.person('two', '000002', 'two')
        self.source(self.record('活動'), self.record('網域', person='two'))
        self.assertEqual(self.active_section().count('[同名成員]'), 2)

    def test_pending_ids_do_not_collapse_people(self):
        self.person('one', '待配置', 'one')
        self.person('two', '待配置', 'two')
        self.source(self.record('活動'), self.record('網域', person='two'))
        self.assertEqual(self.active_section().count('[同名成員]'), 2)

    def test_duplicate_identity_rejected(self):
        for member_id, github in [('000001', 'two'), ('000002', 'ONE')]:
            with self.subTest(member_id=member_id, github=github):
                self.person('two', member_id, github)
                self.source(self.record())
                with self.assertRaises(InvalidSource):
                    render(self.root)

    def test_cutoff_mismatch_excluded_from_active(self):
        for cutoff in ['2026-10-31T14:50:00+08:00', '2026-11-02T14:50:00+08:00']:
            with self.subTest(cutoff=cutoff):
                self.source(self.record(cutoff=cutoff))
                self.assertNotIn('[同名成員]', self.active_section())
                self.assertIn('[同名成員]', render(self.root).split('## 待更新')[1])

    def test_future_active_rejected(self):
        self.source(self.record(effective='2026-11-02T00:00:00+08:00'))
        with self.assertRaises(InvalidSource):
            render(self.root)

    def test_no_automatic_activation(self):
        self.source(self.record(state='尚未生效'))
        self.assertNotIn('[同名成員]', self.active_section())
        self.assertIn('[同名成員]', render(self.root).split('## 尚未生效的安排')[1])

    def test_missing_evidence_rejected(self):
        self.source(self.record().replace('[接受](https://example.com/acceptance)', '口頭聽說'))
        with self.assertRaises(InvalidSource):
            render(self.root)

    def test_conflicting_leaders_rejected(self):
        self.person('two', '000002', 'two')
        second = self.record(person='two').split('### Leader\n')[1]
        self.source(self.record() + second)
        with self.assertRaises(InvalidSource):
            render(self.root)

    def test_failure_preserves_previous_view(self):
        self.source(self.record())
        self.assertEqual(self.run_cli(), 0)
        output = self.root / 'members/council.md'
        original = output.read_bytes()
        self.source(self.record().replace('- 核對結果：已生效', '- 核對結果：猜測'))
        self.assertEqual(self.run_cli(), 2)
        self.assertEqual(output.read_bytes(), original)

    def test_check_detects_manual_and_source_changes(self):
        self.source(self.record())
        self.assertEqual(self.run_cli('--check'), 1)
        self.assertEqual(self.run_cli(), 0)
        self.assertEqual(self.run_cli('--check'), 0)
        output = self.root / 'members/council.md'
        output.write_text(output.read_text() + '手填\n')
        self.assertEqual(self.run_cli('--check'), 1)
        self.assertEqual(self.run_cli(), 0)
        self.person('one', '000001', 'one', name='改稱呼')
        self.assertEqual(self.run_cli('--check'), 1)

    def test_unrelated_intro_and_contributor_do_not_change_view(self):
        self.source(self.record())
        original = render(self.root)
        self.person('new', '待配置', 'new')
        path = self.root / 'members/one.md'
        path.write_text(path.read_text() + '\n## 背景\n新的自介內容\n')
        path = self.root / 'members/r-and-r-assignment.md'
        path.write_text(path.read_text() + '\n### Contributors\n- [新人](new.md)\n')
        self.assertEqual(render(self.root), original)

    def test_unknown_is_not_no_council(self):
        self.source(self.record(state='依據待核對', effective='未定'))
        self.assertIn('不能據此判定沒有 Council', self.active_section())

    def test_person_outside_members_rejected(self):
        self.source(self.record().replace('(one.md)', '(../outside.md)'))
        (self.root / 'outside.md').write_text('# 外部')
        with self.assertRaises(InvalidSource):
            render(self.root)


if __name__ == '__main__':
    unittest.main()
