"""唯讀檢查分工資料與引用；不裁決資格、不改名單或平台權限。"""
import re
import sys
from pathlib import Path, PurePosixPath
from urllib.parse import unquote

import yaml


class UniqueLoader(yaml.SafeLoader):
    pass


def mapping(loader, node):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        if not isinstance(key, str):
            raise ValueError('YAML key 必須是字串')
        if key in result:
            raise ValueError(f'重複 YAML key: {key}')
        result[key] = loader.construct_object(value_node)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def member_path(root, value):
    require(isinstance(value, str) and bool(value), '成員路徑須為非空字串')
    path = PurePosixPath(value)
    require(len(path.parts) == 2 and path.parts[0] == 'members'
            and path.suffix == '.md' and str(path) == value and '\\' not in value,
            f'無效成員路徑: {value}')
    require(path.name.lower() != 'readme.md', f'不是個人成員檔案: {value}')
    target = root / value
    require(target.is_file() and not target.is_symlink(), f'成員檔案不存在或是 symlink: {value}')
    return target


def validate(root):
    root = Path(root)
    data = yaml.load((root / 'members/r-and-r-assignment.yml').read_text(), Loader=UniqueLoader)
    require(isinstance(data, dict) and set(data) == {'assignments'}, '根欄位只允許 assignments')
    rows = data['assignments']
    require(isinstance(rows, list), 'assignments 必須為清單')
    index = (root / 'specs/02-R&R/README.md').read_text()
    entries = re.findall(r'^\| \[([^\]]+)\]\(<?(\[Role\][^>\n]+?\.md)>?\)', index, re.M)
    require(bool(entries), 'R&R 入口沒有可辨識的 Role')
    expected = {name for name, _ in entries}
    require(len(expected) == len(entries), 'R&R 入口名稱重複')
    for name, link in entries:
        require((root / 'specs/02-R&R' / unquote(link)).is_file(), f'Role 文件不存在: {name}')
    seen = set()
    for row in rows:
        require(isinstance(row, dict) and set(row) == {'role', 'leader', 'contributors'},
                '每筆只允許且必須填 role、leader、contributors')
        role = row['role']
        require(isinstance(role, str) and role in expected, f'未知 role: {role!r}')
        require(role not in seen, f'重複 role: {role}')
        seen.add(role)
        if row['leader'] is not None:
            member_path(root, row['leader'])
        people = row['contributors']
        require(isinstance(people, list), f'{role}: contributors 必須為清單')
        unique = set()
        for person in people:
            member_path(root, person)
            require(person not in unique, f'{role}: contributors 重複 {person}')
            unique.add(person)
    require(seen == expected, f'缺少 R&R: {sorted(expected - seen)}')

    # 僅解析「成員資料」中的 YAML 區塊，不把自介其他範例誤認為帳號對應。
    ids = {}
    for path in sorted((root / 'members').glob('*.md')):
        if path.name.lower() == 'readme.md':
            continue
        section = re.search(r'^## 成員資料\s*\n(.*?)(?=^## |\Z)', path.read_text(), re.M | re.S)
        if not section:
            continue
        found = False
        for block in re.findall(r'^```ya?ml\s*\n(.*?)^```\s*$', section[1], re.M | re.S):
            fields = yaml.load(block, Loader=UniqueLoader)
            if not isinstance(fields, dict) or 'discord_id' not in fields:
                continue
            require(not found, f'{path.name}: discord_id 只能填一次')
            found = True
            value = fields['discord_id']
            if value is None:
                continue
            require(isinstance(value, str) and re.fullmatch(r'[0-9]+', value),
                    f'{path.name}: discord_id 必須為數字字串或 null')
            require(value not in ids, f'{path.name}: discord_id 與 {ids.get(value)} 重複')
            ids[value] = path.name
    return len(rows), sum(len(row['contributors']) for row in rows), len(ids)


if __name__ == '__main__':
    try:
        counts = validate(Path(__file__).resolve().parents[1])
    except (ValueError, OSError, yaml.YAMLError) as error:
        print(f'驗證失敗: {error}', file=sys.stderr)
        sys.exit(1)
    print(f'驗證通過：{counts[0]} 項 R&R、{counts[1]} 筆 Contributors、{counts[2]} 筆 Discord ID；未判定任命效力。')
