#!/usr/bin/env python3
"""Render the Council reading view. No network, identity adjudication or role changes."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tempfile
from datetime import datetime, timedelta

FIELDS = ('人員', '決定依據', '本人接受', '生效條件', '生效時間', '核對截止', '本次核對', '核對結果', '尚未完成')
STATES = {'已生效', '尚未生效', '依據待核對', '已終止'}
LINK = re.compile(r'\[([^\]]+)\]\((?:<([^>]+)>|([^\s)]+))\)')
NOTE = 'Verify note：Council 必須至少擔任一項有效的 R&R Leader。'

class InvalidSource(ValueError):
    pass


def instant(value: str) -> datetime:
    try:
        result = datetime.fromisoformat(value)
    except ValueError as exc:
        raise InvalidSource(f'時間須為 ISO 8601：{value}') from exc
    if result.tzinfo is None or result.utcoffset() != timedelta(hours=8):
        raise InvalidSource(f'時間須明列 +08:00：{value}')
    return result


def scalar(text: str, field: str) -> str:
    found = re.findall(rf'^{re.escape(field)}[：:]\s*(.+)$', text, re.M)
    if len(found) != 1:
        raise InvalidSource(f'{field} 須且只能有一個值')
    return found[0].strip()


def safe_person(root: Path, value: str) -> Path:
    matches = list(LINK.finditer(value))
    if len(matches) != 1:
        raise InvalidSource('人員須有且只有一個個人成員檔案連結')
    target = matches[0].group(2) or matches[0].group(3)
    if '#' in target or '?' in target or '://' in target:
        raise InvalidSource('人員必須引用 members 內的本地個人檔案')
    path = (root / 'members' / target).resolve()
    if path.parent != (root / 'members').resolve() or not path.is_file():
        raise InvalidSource(f'個人成員檔案不存在或超出 members：{target}')
    return path


def validate_local_links(root: Path, value: str) -> None:
    for match in LINK.finditer(value):
        target = (match.group(2) or match.group(3)).split('#')[0]
        if not target or target.startswith(('https://', 'http://')):
            continue
        path = (root / 'members' / target).resolve()
        if not path.is_relative_to(root) or not path.exists():
            raise InvalidSource(f'本地來源連結不存在或超出 repo：{target}')


def load(root: Path):
    root = root.resolve()
    assignment = root / 'members/r-and-r-assignment.md'
    text = assignment.read_text(encoding='utf-8')
    cutoff_text = scalar(text, 'Council 核對截止')
    cutoff = instant(cutoff_text)
    people, ids, accounts, identities = {}, {}, {}, {}
    for path in sorted((root / 'members').glob('*.md')):
        if path.name in {'README.md', 'council.md', 'r-and-r-assignment.md'}:
            continue
        body = path.read_text(encoding='utf-8')
        if not re.search(r'^Member ID[：:]', body, re.M):
            continue
        member_id, github = scalar(body, 'Member ID'), scalar(body, 'GitHub')
        title = re.search(r'^# (.+)$', body, re.M)
        if not title:
            raise InvalidSource(f'{path.name} 缺少本人稱呼標題')
        match = LINK.fullmatch(github)
        if match:
            github = match.group(1)
        if not re.fullmatch(r'[A-Za-z0-9-]+', github):
            raise InvalidSource(f'{path.name} GitHub 帳號格式不明')
        account = github.lower()
        if account in accounts:
            raise InvalidSource(f'GitHub 帳號重複，需核對同一人：{path.name}、{accounts[account]}')
        accounts[account] = path.name
        if member_id != '待配置':
            if not re.fullmatch(r'\d{6}', member_id):
                raise InvalidSource(f'{path.name} Member ID 須為既有六位數字或待配置')
            if member_id in ids:
                raise InvalidSource(f'Member ID 重複：{path.name}、{ids[member_id]}')
            ids[member_id] = path.name
        identities[path.name] = (member_id, title.group(1), account)
        # Preserve existing IDs (including the documented founder exception); never allocate IDs.
        people[path.resolve()] = (member_id if member_id != '待配置' else path.relative_to(root).as_posix(), title.group(1))
    records, vacant = [], []
    sections = re.split(r'^## (.+)\s*$', text, flags=re.M)
    for i in range(1, len(sections), 2):
        role, section = sections[i].strip(), sections[i + 1]
        leaders = re.findall(r'^### Leader\s*\n(.*?)(?=^### |\Z)', section, re.M | re.S)
        if not leaders:
            if role != '填寫方式':
                raise InvalidSource(f'{role} 缺少 Leader 區塊')
            continue
        if len(leaders) != 1:
            raise InvalidSource(f'{role} 有重複 Leader 區塊')
        value = leaders[0].strip()
        # Existing HTML anchors belong to the following role and are not assignment data.
        value = re.sub(r'<a id="[^"]+"></a>', '', value).strip()
        if value == '待確認':
            vacant.append(role)
            continue
        blocks = re.split(r'(?=^- 人員：)', value, flags=re.M)
        for block in blocks:
            if not block.strip():
                continue
            row = {}
            for line in block.splitlines():
                if not line.strip():
                    continue
                m = re.fullmatch(r'- ([^：]+)：(.+)', line)
                if not m or m.group(1) not in FIELDS or m.group(1) in row:
                    raise InvalidSource(f'{role} 不支援或重複的 Leader 欄位：{line}')
                row[m.group(1)] = m.group(2).strip()
            if set(row) != set(FIELDS) or any(not value for value in row.values()):
                raise InvalidSource(f'{role} Leader 欄位不完整')
            for value in row.values():
                validate_local_links(root, value)
            path = safe_person(root, row['人員'])
            if path not in people:
                raise InvalidSource(f'{path.name} 缺少可核對的個人資料')
            row['person_key'], row['name'] = people[path]
            row['path'], row['role'] = path.name, role
            row['cutoff'] = instant(row['核對截止'])
            if row['核對結果'] not in STATES:
                raise InvalidSource(f'{role} 不支援的核對結果')
            effective = None if row['生效時間'] == '未定' else instant(row['生效時間'])
            if row['核對結果'] == '已生效':
                if effective is None or effective > row['cutoff']:
                    raise InvalidSource(f'{role} 已生效的時間不成立')
                for key in ('決定依據', '本人接受', '本次核對'):
                    if not LINK.search(row[key]):
                        raise InvalidSource(f'{role} 已生效但缺少 {key} 來源連結')
            records.append(row)
    if not records and not vacant:
        raise InvalidSource('沒有可辨識的 R&R Leader 區塊；停止產生以免覆蓋名單')
    active_by_role = {}
    for row in records:
        if row['cutoff'] == cutoff and row['核對結果'] == '已生效':
            if row['role'] in active_by_role:
                raise InvalidSource(f"{row['role']} 同一截止有兩筆已生效安排，須核對原案")
            active_by_role[row['role']] = row
    # Only Council inputs affect its view; ordinary intros/Contributors stay independent.
    inputs = {'cutoff': cutoff_text, 'vacant': vacant, 'records': [
        {**{field: row[field] for field in FIELDS}, 'role': row['role'],
         'identity': identities[row['path']]} for row in records]}
    digest = hashlib.sha256(json.dumps(inputs, ensure_ascii=False, sort_keys=True).encode('utf-8'))
    return cutoff_text, cutoff, records, vacant, digest.hexdigest()


def cell(value: str) -> str:
    return value.replace('|', '&#124;').replace('\n', ' ')


def render(root: Path) -> str:
    cutoff_text, cutoff, rows, vacant, fingerprint = load(root)
    active, pending, unknown, stale = {}, [], [], []
    for row in rows:
        if row['cutoff'] != cutoff:
            stale.append(row)
        elif row['核對結果'] == '已生效':
            active.setdefault(row['person_key'], []).append(row)
        elif row['核對結果'] == '尚未生效':
            pending.append(row)
        elif row['核對結果'] == '依據待核對':
            unknown.append(row)
    incomplete = bool(stale or unknown or vacant)
    lines = [
        '# Council 名單與分工', '', NOTE, '',
        f'共同核對截止：{cutoff_text}', '',
        '本頁由 [R&R assignment](r-and-r-assignment.md) 與個人成員檔案產生，不能手填。任職以有效原案為準；這不是即時名冊，也不直接作為投票分母。', '',
        f'完整性：{"仍有待核對／待更新事項，不代表全體 Council 名單已完整。" if incomplete else "所列來源在共同截止的核對輸入已齊；原案效力與後續事件仍須由人核對。"}', '',
        f'來源內容 SHA-256：`{fingerprint}`', '',
        '更正請修改 assignment 並引用原案；不需特定管理者同意才能提出疑點。操作方式見 [成員資料說明](README.md#council-名單與維護)。', '',
        '## 截至核對時間可確認的 Council', '',
    ]
    if active:
        lines += ['| 人 | 全部有效 Leader 職位 | 決定與接受依據 | 生效時間 |', '|---|---|---|---|']
        for key, roles in sorted(active.items(), key=lambda x: x[0]):
            first = roles[0]
            values = [f"[{first['name']}]({first['path']})", '<br>'.join(r['role'] for r in roles), '<br>'.join(f"{r['role']}：{r['決定依據']}；{r['本人接受']}；{r['本次核對']}" for r in roles), '<br>'.join(f"{r['role']}：{r['生效時間']}" for r in roles)]
            lines.append('| ' + ' | '.join(map(cell, values)) + ' |')
    else:
        lines.append('尚無足以列入已核對區的資料，不能據此判定沒有 Council。' if incomplete or pending else '截至核對時間未有有效 Council。')
    for title, items in [('尚未生效的安排', pending), ('任職依據待核對', unknown), ('待更新', stale)]:
        lines += ['', f'## {title}', '']
        if not items:
            lines.append('本次輸入沒有此類紀錄；不代表未登錄的外部事件不存在。')
            continue
        lines += ['| 人 | 職位 | 原核對截止與結果 | 依據、條件與下一步 |', '|---|---|---|---|']
        for row in items:
            values = [f"[{row['name']}]({row['path']})", row['role'], f"{row['核對截止']}；{row['核對結果']}", f"決定：{row['決定依據']}；接受：{row['本人接受']}；條件：{row['生效條件']}；生效：{row['生效時間']}；核對：{row['本次核對']}；下一步：{row['尚未完成']}"]
            lines.append('| ' + ' | '.join(map(cell, values)) + ' |')
    if vacant:
        lines += ['', '尚未確認人選的 R&R：' + '、'.join(vacant) + '。這些欄位仍須核對，不能由「待確認」推定有效職位已不存在。']
    return '\n'.join(lines) + '\n'


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--check', action='store_true', help='只讀核對來源和產生檔')
    args = parser.parse_args(argv)
    try:
        output = render(args.root.resolve())
        path = args.root / 'members/council.md'
        if args.check:
            if not path.exists() or path.read_text(encoding='utf-8') != output:
                print('Council 表與來源不同或尚未產生。請先核對原案，再執行 python3 scripts/render_council.py。', file=sys.stderr)
                return 1
            print('Council 表與來源一致；此檢查不判定任職效力或外部事件是否完整。')
        else:
            # Validate and build completely before replacing the existing view.
            with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', dir=path.parent, delete=False) as temp:
                temp.write(output)
                temp_path = temp.name
            os.replace(temp_path, path)
            print(f'已產生 {path}')
        return 0
    except (InvalidSource, OSError) as exc:
        print(f'未改動 Council 表：{exc}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
