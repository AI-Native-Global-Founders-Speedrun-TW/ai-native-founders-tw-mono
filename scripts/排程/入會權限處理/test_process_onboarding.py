"""Offline behavioral tests: all GitHub requests are simulated."""
import copy
import json
import unittest
from unittest.mock import patch

from scripts.排程.入會權限處理.process_onboarding import APIError, ASSIGNMENT, MARKER, ORG, REPO, RECEIPT, GitHub, Manual, Sync, login_from, main

PATH = 'members/000010-alice-Alice.md'
LEADER = 'members/000011-bob-Bob.md'
BOT = 'onboard-test[bot]'
START = '2026-11-01T00:00:00Z'


def assignment(include=True, leader=LEADER):
    import yaml
    return yaml.safe_dump({'assignments': [{'role': 'Onboard／篩選', 'leader': leader,
                                           'contributors': [PATH] if include else []}]})


class FakeAPI:
    def __init__(self):
        self.writes = []
        self.member = None
        self.pending = []
        self.failed = []
        self.comments = []
        self.inline = []
        self.fail_invite = False
        self.fail_comment = False
        self.pr = {'number': 1, 'merged': True, 'merged_at': '2026-11-01T01:00:00Z',
                   'changed_files': 2, 'user': {'login': 'alice', 'id': 10},
                   'head': {'sha': 'head'}, 'base': {'sha': 'base', 'ref': 'main', 'repo': {'full_name': REPO}}}
        self.files = [{'filename': PATH, 'status': 'added'}, {'filename': ASSIGNMENT, 'status': 'modified'}]
        self.reviews = [{'id': 1, 'state': 'APPROVED', 'commit_id': 'head',
                         'submitted_at': '2026-11-01T00:30:00Z', 'user': {'login': 'bob', 'type': 'User'}}]
        self.contents = {(PATH, 'head'): '# Alice\nGitHub：alice\n', (PATH, 'main'): '# Alice\nGitHub：alice\n',
                         (LEADER, 'main'): 'GitHub：bob\n',
                         (ASSIGNMENT, 'base'): assignment(False),
                         (ASSIGNMENT, 'head'): assignment(), (ASSIGNMENT, 'main'): assignment()}
        self.previous = []
        self.timeline = []
        self.label_exists = False

    def content(self, path, ref):
        return self.contents.get((path, ref))

    def pages(self, path):
        if path.endswith('/timeline'):
            return copy.deepcopy(self.timeline)
        if '/pulls?state=' in path:
            return [copy.deepcopy(self.pr)]
        if path.endswith('/files'):
            return copy.deepcopy(self.files)
        if path.endswith('/reviews'):
            return copy.deepcopy(self.reviews)
        if '/pulls/' in path and path.endswith('/comments'):
            return copy.deepcopy(self.inline)
        if path.endswith('/comments'):
            return copy.deepcopy(self.comments)
        if path.endswith('/failed_invitations'):
            return copy.deepcopy(self.failed)
        if path.endswith('/invitations'):
            return copy.deepcopy(self.pending)
        raise AssertionError(path)

    def request(self, method, path, data=None, missing=False):
        if method == 'GET':
            if '/labels/' in path:
                return {'name': RECEIPT} if self.label_exists else None
            if path.endswith('/branches/main'):
                return {'commit': {'sha': 'main'}}
            if path.endswith('/pulls/1'):
                return copy.deepcopy(self.pr)
            if '/contents/members?' in path:
                return copy.deepcopy(self.previous)
            if path == '/users/alice':
                return {'login': 'alice', 'id': 10, 'type': 'User'}
            if '/memberships/' in path:
                return copy.deepcopy(self.member)
            raise AssertionError(path)
        self.writes.append((method, path, data))
        if path.endswith('/labels'):
            if '/issues/' in path:
                self.pr['labels'] = [{'name': RECEIPT}]
                self.timeline.append({'event': 'labeled', 'label': {'name': RECEIPT}, 'actor': {'login': BOT}})
            self.label_exists = True
            return {'name': RECEIPT}
        if path.endswith('/invitations'):
            if self.fail_invite:
                raise APIError(422 if self.fail_invite == '422' else 'timeout')
            self.pending = [{'login': 'alice', 'role': 'direct_member', 'team_count': 0}]
            return {'id': 500}
        if '/comments' in path:
            if self.fail_comment:
                raise APIError('timeout')
            comment = {'id': 100, 'body': data['body'], 'user': {'login': BOT, 'type': 'Bot'},
                       'created_at': START}
            self.comments = [comment]
            return copy.deepcopy(comment)
        raise AssertionError(path)


class SyncTests(unittest.TestCase):
    def setUp(self):
        self.api = FakeAPI()

    def run_sync(self, apply=False):
        return Sync(self.api, START, BOT, apply).run()

    def test_dry_run_is_read_only(self):
        self.assertEqual(self.run_sync(), [(1, 'would-invite')])
        self.assertEqual(self.api.writes, [])

    def test_invite_then_repeat_then_accept(self):
        self.assertEqual(self.run_sync(True), [(1, 'pending')])
        invite = [w for w in self.api.writes if w[1].endswith('/invitations')]
        self.assertEqual(invite[0][2], {'invitee_id': 10, 'role': 'direct_member', 'team_ids': []})
        count = len(self.api.writes)
        self.run_sync(True)
        self.assertEqual(len(self.api.writes), count)
        self.api.member = {'state': 'active'}
        self.api.comments.append({'id': 101, 'body': 'accepted', 'user': {'login': 'alice', 'type': 'User'},
                                  'created_at': '2026-11-01T02:00:00Z'})
        self.assertEqual(self.run_sync(True), [(1, 'joined')])
        count = len(self.api.writes)
        self.run_sync(True)
        self.assertEqual(len(self.api.writes), count)

    def test_existing_member_no_invitation(self):
        self.api.member = {'state': 'active'}
        self.assertEqual(self.run_sync(True), [(1, 'joined')])
        self.assertFalse(any(w[1].endswith('/invitations') for w in self.api.writes))
        self.assertNotIn('<本人', self.api.comments[0]['body'])
        self.assertIn('pullrequestreview-1', self.api.comments[0]['body'])

    def test_closed_unmerged_and_historical_ignored(self):
        self.api.pr['merged_at'] = None
        self.assertEqual(self.run_sync(True), [])
        self.api.pr['merged_at'] = '2020-01-01T00:00:00Z'
        self.assertEqual(self.run_sync(True), [])
        self.assertEqual(self.api.writes, [])

    def test_wrong_repo_or_base_ignored(self):
        self.api.pr['base']['repo']['full_name'] = 'other/repo'
        self.assertEqual(self.run_sync(True), [])

    def test_invite_timeout_leaves_attempt_and_does_not_retry(self):
        self.api.fail_invite = True
        with self.assertRaises(APIError):
            self.run_sync(True)
        self.api.fail_invite = False
        self.assertIn('manual:', self.run_sync(True)[0][1])
        self.assertEqual(len([w for w in self.api.writes if w[1].endswith('/invitations')]), 1)

    def test_marker_write_failure_never_sends_invite(self):
        self.api.fail_comment = True
        with self.assertRaises(APIError):
            self.run_sync(True)
        self.assertFalse(any(w[1].endswith('/invitations') for w in self.api.writes))

    def test_expired_cancelled_and_departed_not_reinvited(self):
        self.run_sync(True)
        self.api.pending = []
        self.assertIn('manual:', self.run_sync(True)[0][1])
        self.api.member = {'state': 'active'}
        self.run_sync(True)
        self.api.member = None
        self.assertIn('manual:', self.run_sync(True)[0][1])
        self.assertEqual(len([w for w in self.api.writes if w[1].endswith('/invitations')]), 1)

    def test_failed_invite_or_wrong_team_goes_manual(self):
        self.api.failed = [{'login': 'alice'}]
        self.assertIn('manual:', self.run_sync(True)[0][1])
        self.api.failed = []
        self.api.pending = [{'login': 'alice', 'role': 'admin', 'team_count': 0}]
        self.assertIn('manual:', self.run_sync(True)[0][1])
        self.assertEqual(self.api.writes, [])

    def test_authorization_failures_never_write(self):
        for scenario in ['no-leader', 'self', 'no-review', 'stale', 'dismissed', 'changes', 'comment', 'inline']:
            with self.subTest(scenario=scenario):
                self.api = FakeAPI()
                if scenario == 'no-leader': self.api.contents[(ASSIGNMENT, 'main')] = assignment(leader=None)
                if scenario == 'self': self.api.contents[(LEADER, 'main')] = 'GitHub：alice'
                if scenario == 'no-review': self.api.reviews = []
                if scenario == 'stale': self.api.reviews[0]['commit_id'] = 'old'
                if scenario == 'dismissed': self.api.reviews[0]['state'] = 'DISMISSED'
                if scenario == 'changes':
                    self.api.reviews.append(dict(self.api.reviews[0], id=2, state='CHANGES_REQUESTED', user={'login': 'charlie', 'type': 'User'}))
                if scenario in ['comment', 'inline']:
                    target = self.api.comments if scenario == 'comment' else self.api.inline
                    target.append({'body': 'question', 'user': {'login': 'alice', 'type': 'User'}, 'created_at': '2026-11-01T02:00:00Z'})
                self.assertIn('manual:', self.run_sync(True)[0][1])
                self.assertEqual(self.api.writes, [])

    def test_pr_scope_and_identity_failures(self):
        for scenario in ['extra-file', 'other-person', 'leader-change', 'missing-current', 'wrong-login', 'truncated']:
            with self.subTest(scenario=scenario):
                self.api = FakeAPI()
                if scenario == 'extra-file':
                    self.api.files.append({'filename': 'scripts/evil.py', 'status': 'added'})
                    self.api.pr['changed_files'] += 1
                if scenario == 'other-person': self.api.contents[(ASSIGNMENT, 'head')] = assignment().replace('contributors:', 'contributors: [someone]\n  unused:')
                if scenario == 'leader-change': self.api.contents[(ASSIGNMENT, 'head')] = assignment(leader=PATH)
                if scenario == 'missing-current': del self.api.contents[(PATH, 'main')]
                if scenario == 'wrong-login': self.api.contents[(PATH, 'head')] = 'GitHub：other'
                if scenario == 'truncated': self.api.pr['changed_files'] = 9
                self.assertIn('manual:', self.run_sync(True)[0][1])
                self.assertEqual(self.api.writes, [])

    def test_preexisting_profile_not_initial_application(self):
        self.api.previous = [{'type': 'file', 'name': 'old.md', 'path': 'members/old.md'}]
        self.api.contents[('members/old.md', 'base')] = 'GitHub：alice'
        self.assertIn('manual:', self.run_sync(True)[0][1])
        self.assertEqual(self.api.writes, [])

    def test_duplicate_or_corrupt_bot_state_stops(self):
        self.run_sync(True)
        self.api.comments.append(copy.deepcopy(self.api.comments[0]))
        self.assertIn('manual:', self.run_sync(True)[0][1])
        self.api.comments = [dict(self.api.comments[0], body=MARKER + '{} -->')]
        self.assertIn('manual:', self.run_sync(True)[0][1])

    def test_deleted_comment_removed_label_still_not_reinvited(self):
        self.run_sync(True)
        self.api.comments = []
        self.api.pending = []
        self.api.pr['labels'] = []
        self.assertIn('manual:', self.run_sync(True)[0][1])
        self.assertEqual(len([w for w in self.api.writes if w[1].endswith('/invitations')]), 1)

    def test_existing_member_without_review_not_welcomed(self):
        self.api.member = {'state': 'active'}
        self.api.reviews = []
        self.assertIn('manual:', self.run_sync(True)[0][1])
        self.assertEqual(self.api.writes, [])

    def test_personal_errors_do_not_stop_next_pr(self):
        for cause in ['yaml', '422']:
            with self.subTest(cause=cause):
                self.api = FakeAPI()
                if cause == 'yaml': self.api.contents[(ASSIGNMENT, 'head')] = '{broken:'
                else: self.api.fail_invite = '422'
                sync = Sync(self.api, START, BOT, True)
                original_pages = self.api.pages
                original_get = sync.get
                self.api.pages = lambda path: [self.api.pr, dict(self.api.pr, number=2)] if '/pulls?state=' in path else original_pages(path)
                sync.get = lambda suffix, missing=False: dict(self.api.pr, number=2) if suffix == 'pulls/2' else original_get(suffix, missing)
                original_process = sync.process
                sync.process = lambda pr: 'second-processed' if pr['number'] == 2 else original_process(pr)
                result = sync.run()
                self.assertTrue(result[0][1].startswith('manual:'))
                self.assertEqual(result[1], (2, 'second-processed'))

    def test_plain_link_and_markdown_login(self):
        for text in ['GitHub：Alice', 'GitHub: https://github.com/Alice', 'GitHub：[Alice](https://github.com/Alice)']:
            self.assertEqual(login_from(text), 'alice')
        with self.assertRaises(Manual): login_from('GitHub: https://example.com/alice')

    def test_cli_ref_and_enable_gate(self):
        with patch.dict('os.environ', {'GITHUB_REF': 'refs/heads/topic', 'ONBOARDING_ENABLED': 'true'}, clear=True), patch('sys.argv', ['sync', '--apply']):
            with self.assertRaises(SystemExit) as result: main()
            self.assertEqual(result.exception.code, 2)


class TransportTests(unittest.TestCase):
    def test_pagination_reads_all_pages(self):
        api = GitHub('not-a-real-token')
        with patch.object(api, 'request', side_effect=[[{'id': n} for n in range(100)], [{'id': 100}]]) as request:
            result = api.pages('/orgs/example/invitations')
        self.assertEqual(len(result), 101)
        self.assertTrue(request.call_args_list[1].args[1].endswith('page=2'))

    def test_partial_page_error_is_not_empty_success(self):
        api = GitHub('not-a-real-token')
        with patch.object(api, 'request', side_effect=[[{}] * 100, APIError(403, '60')]):
            with self.assertRaises(APIError): api.pages('/orgs/example/invitations')

    def test_http_errors_do_not_expose_payload_or_token(self):
        from io import BytesIO
        from urllib.error import HTTPError
        api = GitHub('private-token')
        error = HTTPError('https://api.github.com/test', 403, 'error', {'Retry-After': '60'}, BytesIO(b'private-email@example.com'))
        with patch('scripts.排程.入會權限處理.process_onboarding.urlopen', side_effect=error):
            with self.assertRaises(APIError) as result: api.request('GET', '/test')
        self.assertEqual(str(result.exception), 'GitHub API HTTP 403; Retry-After=60')

    def test_only_explicit_missing_404_is_absence(self):
        from urllib.error import HTTPError
        api = GitHub('not-a-real-token')
        with patch('scripts.排程.入會權限處理.process_onboarding.urlopen', side_effect=HTTPError('url', 404, 'missing', {}, None)):
            self.assertIsNone(api.request('GET', '/test', missing=True))
            with self.assertRaises(APIError): api.request('GET', '/test')


if __name__ == '__main__':
    unittest.main()
