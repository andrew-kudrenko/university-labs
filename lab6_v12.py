from typing import List, Dict, Optional


def compare(lexems: List[str], lines: List[str]) -> bool:
    for line in lines:
        for lexeme in line.split():
            if lexeme in lexems:
                return True

    return False


def identify_lang(lexems: Dict[str, List[str]], lines: List[str]) -> Optional[Dict[str, bool]]:
    for lang in lexems:
        asserted = compare(lexems[lang], lines)

        if asserted:
            return lang

    return


def get_input() -> List[str]:
    rows: int = int(input('Enter a rows count: '))

    return [input('> ') for _ in range(rows)]


lexems: Dict[str, List[str]] = {
    'php': ['<?php', '?>'],
    'javascript': ['let', 'const'],
    'lua': ['::=']
}

lines = get_input()

identified_lang: Optional[str] = identify_lang(lexems, lines)

print('Unknown' if not identified_lang else identified_lang)
