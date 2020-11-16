from typing import Dict, List


def has_all_exclude_first(player: str, trophies: Dict[str, List[str]]) -> bool:
    for i, key in enumerate(list(trophies.keys())):
        if i == 0:
            if player in trophies[key]:
                return False
            else:
                continue

        if player not in trophies[key]:
            return False

    return True


def parse_input_to_dict(data: str) -> Dict[str, List[str]]:
    key, values = data.split(':')
    trimmed_values: List[str] = list(map(lambda s: s.strip(), values.split(',')))

    return {key: trimmed_values}


def get_key(index: int, dict: Dict) -> any:
    return list(dict.keys())[index]


trophies: Dict[str, List[str]] = {}
players: List[str] = []

rows: int = int(input('Enter rows count: '))
found: List[str] = []

print('Enter rows for creating a dictionary')

for i in range(rows):
    current: str = input('> ')
    parsed = parse_input_to_dict(current)
    key: str = get_key(0, parsed)

    trophies[key] = parsed[key]
    players += parsed[key]


print(f'Dictionary: {trophies}')
print(f'Players: {players}')

for p in players:
    has = has_all_exclude_first(p, trophies)

    if has:
        found.append(p)

print(f'Has all, exclude first: {found}')

# Excepts string as 'key: 0, 1, 2, 3, 4'
# [key]: [values, separated by comma]

# Example for test

# trophies: Dict[str, List[str]] = {
#     'second': ['p1', 'p2'],
#     'fourth': ['p2', 'p3', 'p4', 'p6'],
#     'third': ['p1', 'p8', 'p6', 'p2']
# }
