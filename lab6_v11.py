from typing import Dict, List


def has_all_exclude_first(player: str, trophies: Dict[str, List[str]]) -> bool:
    for i, key in enumerate(trophies.keys()):
        if i == 0:
            if player in trophies[key]:
                return False
            else:
                continue

        if player not in trophies[key]:
            return False

    return True


def parse_input(data: str) -> Dict[str, List[str]]:
    key, values = data.split(':')
    trimmed_values: List[str] = list(map(lambda s: s.strip(), values.split(',')))

    return {key: trimmed_values}


def get_key(index: int, dict: Dict) -> any:
    return list(dict.keys())[index]


def filter_players(players: List[str], trophies: Dict[str, List[str]]) -> List[str]:
    found: List[str] = []

    for p in players:
        has = has_all_exclude_first(p, trophies)

        if has and p not in found:
            found.append(p)

    return found


def input_dict(rows: int):
    trophies = {}

    for i in range(rows):
        current: str = input('> ')
        parsed = parse_input(current)
        key: str = get_key(0, parsed)

        trophies[key] = parsed[key]

    return trophies


def extract_players(trophies: Dict[str, List[str]]) -> List[str]:
    players: List[str] = []

    for _, key in enumerate(trophies):
        for player in trophies[key]:
            if player not in players:
                players.append(player)

    return players


print('Enter rows for creating a dictionary')

trophies: Dict[str, List[str]] = input_dict(int(input('Enter rows count: ')))
players: List[str] = extract_players(trophies)

print(f'Has all, exclude first: {filter_players(players, trophies)}')

# Excepts string as 'key: 0, 1, 2, 3, 4'
# [key]: [values, separated by comma]

# Example for test

# trophies: Dict[str, List[str]] = {
#     'second': ['p1', 'p2'],
#     'fourth': ['p2', 'p3', 'p4', 'p6'],
#     'third': ['p1', 'p8', 'p6', 'p2']
# }
