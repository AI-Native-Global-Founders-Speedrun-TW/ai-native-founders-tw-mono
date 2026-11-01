import tempfile
import unittest
from pathlib import Path

from validate_assignments import validate


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / 'members').mkdir()
        roles = self.root / 'specs/02-R&R'
        roles.mkdir(parents=True)
        (roles / 'README.md').write_text('| [Hacker](<[Role]Hacker.md>) | 職責 |\n')
        (roles / '[Role]Hacker.md').write_text('# Hacker')
        self.member('alice', None)
        self.member('bob', None)
        self.good = 'assignments:\n- role: Hacker\n  leader: members/alice.md\n  contributors: [members/bob.md]\n'
        self.write(self.good)

    def member(self, name, value):
        text = '# Person\n\n## 成員資料\n'
        if value is not None:
            text += f'```yaml\ndiscord_id: {value}\n```\n'
        (self.root / f'members/{name}.md').write_text(text)

    def write(self, text):
        (self.root / 'members/r-and-r-assignment.yml').write_text(text)

    def test_valid_and_no_mutation(self):
        self.assertEqual(validate(self.root), (1, 1, 0))
        self.assertEqual((self.root / 'members/r-and-r-assignment.yml').read_text(), self.good)

    def test_null_leader(self):
        self.write(self.good.replace('leader: members/alice.md', 'leader: null'))
        validate(self.root)

    def test_invalid_data(self):
        cases = [
            self.good + 'assignments: []\n',
            self.good.replace('  leader:', '  role: Hacker\n  leader:'),
            self.good.replace('Hacker', 'Unknown'),
            'assignments: []\n',
            self.good + self.good.split('assignments:\n')[1],
            self.good.replace('members/alice.md', '../alice.md'),
            self.good.replace('members/alice.md', 'members/missing.md'),
            self.good.replace('members/alice.md', 'false'),
            self.good.replace('[members/bob.md]', '[members/bob.md, members/bob.md]'),
            self.good.replace('[members/bob.md]', 'null'),
            self.good.replace('  leader: members/alice.md\n', ''),
            self.good + '  extra: value\n',
            'assignments: [\n',
        ]
        for text in cases:
            with self.subTest(text=text):
                self.write(text)
                with self.assertRaises(Exception):
                    validate(self.root)

    def test_discord_string_and_null(self):
        self.member('alice', '"123456789012345678"')
        self.member('bob', 'null')
        self.assertEqual(validate(self.root)[2], 1)

    def test_invalid_discord(self):
        for value in ['123456789012345678', '"@alice"', '""', 'false']:
            with self.subTest(value=value):
                self.member('alice', value)
                with self.assertRaises(ValueError):
                    validate(self.root)

    def test_duplicate_discord(self):
        self.member('alice', '"123"')
        self.member('bob', '"123"')
        with self.assertRaises(ValueError):
            validate(self.root)

    def test_discord_outside_member_data_is_ignored(self):
        p = self.root / 'members/alice.md'
        p.write_text(p.read_text() + '\n## 範例\n```yaml\ndiscord_id: 123\n```\n')
        self.assertEqual(validate(self.root)[2], 0)

    def test_duplicate_discord_keys(self):
        self.member('alice', '"123"\ndiscord_id: "456"')
        with self.assertRaises(ValueError):
            validate(self.root)

    def test_unclosed_member_fence(self):
        p = self.root / 'members/alice.md'
        p.write_text('# Person\n## 成員資料\n```yaml\ndiscord_id: 123\n')
        with self.assertRaisesRegex(ValueError, '未關閉'):
            validate(self.root)

    def test_duplicate_member_section(self):
        self.member('alice', '"123"')
        p = self.root / 'members/alice.md'
        p.write_text(p.read_text() + '\n## 成員資料\n```yaml\ndiscord_id: "456"\n```\n')
        with self.assertRaisesRegex(ValueError, '章節重複'):
            validate(self.root)

    def test_markdown_fence_variants(self):
        for fence in ['````', '~~~', '~~~~']:
            with self.subTest(fence=fence):
                p = self.root / 'members/alice.md'
                p.write_text(f'# Person\n## 成員資料\n{fence}yaml\ndiscord_id: false\n{fence}\n')
                with self.assertRaisesRegex(ValueError, '數字字串'):
                    validate(self.root)
                p.write_text(f'# Person\n## 成員資料\n{fence}yml\ndiscord_id: "123"\n{fence}\n')
                self.assertEqual(validate(self.root)[2], 1)

    def test_mismatched_fence(self):
        p = self.root / 'members/alice.md'
        p.write_text('# Person\n## 成員資料\n````yaml\ndiscord_id: "123"\n```\n')
        with self.assertRaisesRegex(ValueError, '未關閉'):
            validate(self.root)


if __name__ == '__main__':
    unittest.main()
