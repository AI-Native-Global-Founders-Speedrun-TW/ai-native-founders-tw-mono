"""Reconcile approved onboarding PRs. Dry-run by default; no governance decisions."""
import argparse
import base64
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen

import yaml
from scripts.驗證.分工資料.validate import UniqueLoader

REPO = 'AI-Native-Global-Founders-Speedrun-TW/ai-native-founders-tw-mono'
ORG = REPO.split('/')[0]
ASSIGNMENT = 'members/r-and-r-assignment.yml'
MARKER = '<!-- onboarding-sync:v1 '
RECEIPT = 'onboarding-started'
MEMBER = re.compile(r'members/\d{6}-[A-Za-z0-9-]+(?:-[^/]+)?\.md\Z')


class APIError(Exception):
    def __init__(self, status, retry_after=None):
        self.status, self.retry_after = status, retry_after
        super().__init__(f'GitHub API HTTP {status}' + (f'; Retry-After={retry_after}' if retry_after else ''))


class Manual(Exception):
    pass


def timestamp(value):
    dt = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if dt.tzinfo is None:
        raise ValueError('Timestamp must include timezone')
    return dt


class GitHub:
    def __init__(self, token):
        self.token = token

    def request(self, method, path, data=None, missing=False):
        if not path.startswith('/') or path.startswith('//'):
            raise ValueError('Only GitHub API paths are allowed')
        req = Request('https://api.github.com' + path,
                      data=json.dumps(data).encode() if data is not None else None,
                      headers={'Authorization': f'Bearer {self.token}',
                               'Accept': 'application/vnd.github+json',
                               'X-GitHub-Api-Version': '2022-11-28'}, method=method)
        try:
            with urlopen(req, timeout=30) as response:
                body = response.read()
                return json.loads(body) if body else None
        except HTTPError as error:
            if missing and error.code == 404:
                return None
            # Never print API bodies, which can contain private data.
            raise APIError(error.code, error.headers.get('Retry-After')) from None
        except (URLError, TimeoutError, json.JSONDecodeError):
            raise APIError('unavailable-or-unknown-result') from None

    def pages(self, path):
        result = []
        for page in range(1, 10001):
            separator = '&' if '?' in path else '?'
            batch = self.request('GET', f'{path}{separator}per_page=100&page={page}')
            if not isinstance(batch, list):
                raise APIError('invalid-list-response')
            result.extend(batch)
            if len(batch) < 100:
                return result
        raise APIError('pagination-limit')

    def content(self, path, ref):
        entry = self.request('GET', f'/repos/{REPO}/contents/{quote(path, safe="/")}?{urlencode({"ref": ref})}', missing=True)
        if entry is None:
            return None
        if entry.get('type') != 'file' or entry.get('encoding') != 'base64':
            raise Manual('檔案不是可讀取的一般檔案')
        return base64.b64decode(entry['content']).decode('utf-8')


def login_from(text):
    """Only the explicit GitHub field, never arbitrary profile links in prose."""
    fields = re.findall(r'^GitHub\s*[：:]\s*(.+)$', text or '', re.M)
    if len(fields) != 1:
        raise Manual('需要唯一的 GitHub 帳號欄位')
    value = fields[0].strip()
    match = re.fullmatch(r'\[.*?\]\(https://github\.com/([A-Za-z0-9-]+)/?\)', value)
    if not match:
        match = re.fullmatch(r'(?:https://github\.com/|@)?([A-Za-z0-9-]+)/?', value)
    if not match:
        raise Manual('GitHub 帳號格式需人工核對')
    return match[1].lower()


def assignments(text):
    try:
        data = yaml.load(text or '', Loader=UniqueLoader)
    except (yaml.YAMLError, ValueError):
        raise Manual('分工 YAML 無法解析') from None
    if not isinstance(data, dict) or set(data) != {'assignments'}:
        raise Manual('分工資料不完整')
    rows = data['assignments']
    if not isinstance(rows, list):
        raise Manual('分工資料不是清單')
    result = {}
    for row in rows:
        if (not isinstance(row, dict) or set(row) != {'role', 'leader', 'contributors'}
                or not isinstance(row['role'], str) or row['role'] in result
                or not isinstance(row['contributors'], list)
                or any(not isinstance(p, str) for p in row['contributors'])
                or len(set(row['contributors'])) != len(row['contributors'])):
            raise Manual('分工資料欄位或重複值不符')
        result[row['role']] = row
    return result


class Sync:
    def __init__(self, api, start, bot, apply=False):
        self.api, self.start, self.bot, self.apply = api, timestamp(start), bot, apply
        self.results = []
        self.main = None

    def get(self, suffix, missing=False):
        return self.api.request('GET', f'/repos/{REPO}/{suffix}', missing=missing)

    def comments(self, number):
        return self.api.pages(f'/repos/{REPO}/issues/{number}/comments')

    def state(self, comments, number, uid):
        found = [c for c in comments if c.get('user', {}).get('login') == self.bot
                 and c['user'].get('type') == 'Bot' and MARKER in c.get('body', '')]
        if len(found) > 1:
            raise Manual('進度留言重複，請人工核對')
        if not found:
            return None, {'pr': number, 'user_id': uid, 'attempted': False, 'completed': False, 'review_id': None, 'member_path': None}
        c = found[0]
        try:
            state = json.loads(c['body'].split(MARKER, 1)[1].split(' -->', 1)[0])
            if (set(state) != {'pr', 'user_id', 'attempted', 'completed', 'status', 'review_id', 'member_path'}
                    or state['pr'] != number or state['user_id'] != uid
                    or type(state['attempted']) is not bool or type(state['completed']) is not bool
                    or type(state['review_id']) is not int or not MEMBER.fullmatch(state['member_path'] or '')):
                raise ValueError()
        except (ValueError, KeyError, IndexError):
            raise Manual('既有進度留言無法核對') from None
        return c, state

    def save(self, number, login, comment, state, status):
        updated = dict(state, status=status)
        if status == 'joined':
            updated['completed'] = True
        messages = {'sending': '準備發送 Member 邀請。',
                    'pending': '邀請已送出，等待本人接受；無須回覆才能確認。',
                    'joined': '🎉 歡迎加入！已確認 GitHub org Member 身分。可繼續以 Fork／PR 參與協作。',
                    'manual': '需要 Onboard 人工核對；不會自動重送邀請或取消資格。'}
        message = self.welcome(login, updated) if status == 'joined' else messages[status]
        body = (f'{MARKER}{json.dumps(updated, sort_keys=True)} -->\n'
                f'GitHub 加入進度：@{login}\n\n{message}\n\n'
                f'[核准 review](https://github.com/{REPO}/pull/{number}#pullrequestreview-{updated["review_id"]}) · '
                f'[組織入口](https://github.com/{ORG}) · '
                f'[參與說明](https://github.com/{REPO}/blob/main/members/README.md)')
        if self.apply and (comment is None or comment['body'] != body):
            if comment is None:
                self.record_receipt(number)
            path = (f'/repos/{REPO}/issues/comments/{comment["id"]}' if comment
                    else f'/repos/{REPO}/issues/{number}/comments')
            comment = self.api.request('PATCH' if comment else 'POST', path, {'body': body})
        return comment, updated

    def welcome(self, login, state):
        root = Path(__file__).resolve().parents[3]
        sop = (root / 'specs/03-SOP/[SOP]自介PR審查SOP.md').read_text()
        section = sop.split('### 歡迎正式加入 GitHub org comment', 1)[1].split('### ', 1)[0]
        template = '\n'.join(line[2:] if line.startswith('> ') else '' for line in section.splitlines() if line.startswith('>'))
        discord_spec = (root / 'specs/05-社群基建/[規格]Discord-社群-Setup.md').read_text()
        match = re.search(r'現行邀請[^\n]*?(https://discord\.gg/[A-Za-z0-9]+)', discord_spec)
        if not match:
            raise Manual('找不到正式 Discord 入口，歡迎留言需人工接續')
        values = {'本人稱呼': login, 'GitHub username': login,
                  '已合併的自介連結': f'https://github.com/{REPO}/blob/main/{quote(state["member_path"], safe="/")}',
                  '本人 assignment 連結': f'https://github.com/{REPO}/blob/main/{ASSIGNMENT}',
                  '實際 Discord 入口連結': match[1],
                  'members README 連結': f'https://github.com/{REPO}/blob/main/members/README.md'}
        for key, value in values.items():
            template = template.replace('<' + key + '>', value)
        if re.search(r'<[^>]+>', template):
            raise Manual('歡迎文案仍有未填欄位')
        return template

    def receipt_exists(self, pr):
        if any(label['name'] == RECEIPT for label in pr.get('labels', [])):
            return True
        timeline = self.api.pages(f'/repos/{REPO}/issues/{pr["number"]}/timeline')
        return any(event.get('event') == 'labeled' and event.get('label', {}).get('name') == RECEIPT
                   and event.get('actor', {}).get('login') == self.bot for event in timeline)

    def record_receipt(self, number):
        path = f'/repos/{REPO}/labels/{RECEIPT}'
        if self.api.request('GET', path, missing=True) is None:
            self.api.request('POST', f'/repos/{REPO}/labels',
                             {'name': RECEIPT, 'color': '7057ff', 'description': 'Automatic onboarding receipt; do not remove'})
        self.api.request('POST', f'/repos/{REPO}/issues/{number}/labels', {'labels': [RECEIPT]})

    def candidate(self, pr, files):
        added = [f['filename'] for f in files if f['status'] == 'added' and MEMBER.fullmatch(f['filename'])]
        if len(added) != 1:
            raise Manual('不是單人初次自介新增；由人工接續')
        path = added[0]
        prefix = path.split('/')[-1][:6] + '-'
        for f in files:
            name = f['filename']
            if name == path:
                continue
            if name == ASSIGNMENT and f['status'] == 'modified':
                continue
            if (name.startswith('members/assets/' + prefix) and name.count('/') == 2
                    and f['status'] == 'added' and name.rsplit('.', 1)[-1] in {'png', 'jpg', 'jpeg', 'webp'}):
                continue
            raise Manual('PR 包含其他人的資料或非入會變更')
        login = login_from(self.api.content(path, pr['head']['sha']))
        if login != pr['user']['login'].lower():
            raise Manual('受邀帳號與 PR 作者不同')
        current = self.api.content(path, self.main)
        if current is None or login_from(current) != login:
            raise Manual('目前 main 成員資料缺失或帳號改變')
        before = assignments(self.api.content(ASSIGNMENT, pr['base']['sha']))
        after = assignments(self.api.content(ASSIGNMENT, pr['head']['sha']))
        if set(before) != set(after):
            raise Manual('PR 修改了職責清單')
        selected = False
        for role, old in before.items():
            new = after[role]
            if (old['leader'] != new['leader'] or path in old['contributors']
                    or [x for x in new['contributors'] if x != path] != old['contributors']):
                raise Manual('PR 修改了他人分工或既有身分')
            selected |= path in new['contributors']
        now = assignments(self.api.content(ASSIGNMENT, self.main))
        if not selected or not any(path in row['contributors'] for row in now.values()):
            raise Manual('沒有本人有效 Contributors 選擇')
        # A previous profile for the same account must never count as a new application.
        entries = self.get(f'contents/members?{urlencode({"ref": pr["base"]["sha"]})}')
        for entry in entries:
            if entry['type'] == 'file' and entry['name'].endswith('.md') and entry['name'].lower() != 'readme.md':
                try:
                    old_login = login_from(self.api.content(entry['path'], pr['base']['sha']))
                except Manual:
                    raise Manual('既有成員帳號無法完整核對') from None
                if old_login == login:
                    raise Manual('已有自介；不是初次申請')
        return path, login, now

    def authorize(self, pr, now, comments):
        leader = now.get('Onboard／篩選', {}).get('leader')
        if not isinstance(leader, str) or not MEMBER.fullmatch(leader):
            raise Manual('Onboard Leader 空缺或資料不明')
        reviewer = login_from(self.api.content(leader, self.main))
        if reviewer == pr['user']['login'].lower():
            raise Manual('不能自審')
        reviews = self.api.pages(f'/repos/{REPO}/pulls/{pr["number"]}/reviews')
        latest = {}
        for review in sorted(reviews, key=lambda x: x['id']):
            if review['state'] in {'APPROVED', 'CHANGES_REQUESTED', 'DISMISSED'}:
                latest[review['user']['login'].lower()] = review
        approval = latest.get(reviewer)
        if (not approval or approval['state'] != 'APPROVED'
                or approval['commit_id'] != pr['head']['sha']):
            raise Manual('沒有目前 Onboard 對最終版本的有效核准')
        if any(x['state'] == 'CHANGES_REQUESTED' for x in latest.values()):
            raise Manual('仍有 Request changes 需人工核對')
        for comment in comments:
            if comment['user'].get('type') != 'Bot' and timestamp(comment.get('updated_at', comment['created_at'])) > timestamp(approval['submitted_at']):
                raise Manual('核准後有新的人類留言，需人工核對')
        for review in reviews:
            if review['user'].get('type') != 'Bot' and review['id'] != approval['id'] and timestamp(review['submitted_at']) > timestamp(approval['submitted_at']):
                raise Manual('核准後有新 review，需人工核對')
        inline = self.api.pages(f'/repos/{REPO}/pulls/{pr["number"]}/comments')
        if any(c['user'].get('type') != 'Bot' and timestamp(c.get('updated_at', c['created_at'])) > timestamp(approval['submitted_at']) for c in inline):
            raise Manual('核准後有程式行留言，需人工核對')
        return approval['id']

    def process(self, pr):
        number = pr['number']
        files = self.api.pages(f'/repos/{REPO}/pulls/{number}/files')
        if len(files) != pr['changed_files']:
            raise Manual('PR 檔案清單不完整')
        if not any(f['filename'].startswith('members/') for f in files):
            return 'skip'
        member_path, login, now = self.candidate(pr, files)
        user = self.api.request('GET', f'/users/{quote(login)}')
        if user['type'] != 'User' or user['id'] != pr['user']['id']:
            raise Manual('GitHub user ID 與作者不符')
        comments = self.comments(number)
        comment, state = self.state(comments, number, user['id'])
        if comment is None:
            if self.receipt_exists(pr):
                raise Manual('有接續收據但進度留言遺失，需人工核對')
            state['review_id'] = self.authorize(pr, now, comments)
            state['member_path'] = member_path
        elif state['member_path'] != member_path:
            raise Manual('進度留言與自介路徑不符')
        membership = self.api.request('GET', f'/orgs/{ORG}/memberships/{quote(login)}', missing=True)
        if membership and membership['state'] == 'active':
            self.save(number, login, comment, state, 'joined')
            return 'joined'
        pending = self.api.pages(f'/orgs/{ORG}/invitations')
        pending = [i for i in pending if (i.get('login') or '').lower() == login]
        if pending:
            if len(pending) != 1 or pending[0]['role'] != 'direct_member' or pending[0]['team_count'] != 0:
                raise Manual('現有邀請的角色或 Team 不符')
            state['attempted'] = True
            self.save(number, login, comment, state, 'pending')
            return 'pending'
        if state['attempted'] or state['completed'] or membership:
            self.save(number, login, comment, state, 'manual')
            raise Manual('曾邀請／完成或平台狀態不明；不可自動重邀')
        failed = self.api.pages(f'/orgs/{ORG}/failed_invitations')
        if any((i.get('login') or '').lower() == login for i in failed):
            raise Manual('有失敗或過期邀請，需人工重邀')
        # A changed profile or missing authorization is never repaired by the automation.
        self.authorize(pr, now, comments)
        if not self.apply:
            return 'would-invite'
        state['attempted'] = True
        comment, state = self.save(number, login, comment, state, 'sending')
        try:
            self.api.request('POST', f'/orgs/{ORG}/invitations',
                             {'invitee_id': user['id'], 'role': 'direct_member', 'team_ids': []})
        except APIError as error:
            if error.status == 422 and not error.retry_after:
                self.save(number, login, comment, state, 'manual')
                raise Manual('GitHub 拒絕此邀請，需人工核對；不自動重送') from None
            raise
        # Read back, not just HTTP success. A failure leaves the durable sending marker.
        member = self.api.request('GET', f'/orgs/{ORG}/memberships/{quote(login)}', missing=True)
        if member and member['state'] == 'active':
            status = 'joined'
        else:
            invitations = self.api.pages(f'/orgs/{ORG}/invitations')
            if not any((i.get('login') or '').lower() == login and i['role'] == 'direct_member' and i['team_count'] == 0 for i in invitations):
                raise Manual('發送後無法確認結果，請人工接續')
            status = 'pending'
        self.save(number, login, comment, state, status)
        return status

    def run(self):
        self.main = self.get('branches/main')['commit']['sha']
        prs = self.api.pages(f'/repos/{REPO}/pulls?state=closed&base=main&sort=created&direction=asc')
        for entry in prs:
            if not entry.get('merged_at') or timestamp(entry['merged_at']) < self.start:
                continue
            pr = self.get(f'pulls/{entry["number"]}')
            if not pr.get('merged') or pr['base']['ref'] != 'main' or pr['base']['repo']['full_name'].lower() != REPO.lower():
                continue
            try:
                result = self.process(pr)
            except (Manual, ValueError, KeyError, TypeError) as error:
                result = 'manual: ' + (str(error) if isinstance(error, Manual) else '資料格式不完整，需人工核對')
            self.results.append((pr['number'], result))
        return self.results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--apply', action='store_true')
    mode.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    if os.environ.get('GITHUB_REPOSITORY', REPO).lower() != REPO.lower():
        parser.error('Unexpected repository')
    if args.apply and (os.environ.get('GITHUB_REF') != 'refs/heads/main' or os.environ.get('ONBOARDING_ENABLED') != 'true'):
        parser.error('Apply requires main and ONBOARDING_ENABLED=true')
    token, start, bot = (os.environ.get(k, '') for k in ('GH_TOKEN', 'ONBOARDING_START_AT', 'ONBOARDING_BOT_LOGIN'))
    if not token or not start or not re.fullmatch(r'[a-z0-9-]+\[bot\]', bot):
        parser.error('GH_TOKEN, ONBOARDING_START_AT and ONBOARDING_BOT_LOGIN are required')
    try:
        sync = Sync(GitHub(token), start, bot, args.apply)
    except ValueError:
        parser.error('ONBOARDING_START_AT must be an ISO 8601 timestamp with timezone')
    code = 0
    try:
        sync.run()
    except APIError as error:
        print(str(error), file=sys.stderr)
        code = 1
    lines = ['## Onboarding ' + ('apply' if args.apply else 'dry-run')]
    lines += [f'- https://github.com/{REPO}/pull/{n}: {result}' for n, result in sync.results]
    if code:
        lines.append('- 本輪未完成：API 失敗，請 Repository 接續；未列出不表示完成。')
    text = '\n'.join(lines) + '\n'
    print(text)
    if os.environ.get('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'], 'a') as output:
            output.write(text)
    return code


if __name__ == '__main__':
    sys.exit(main())
