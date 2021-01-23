def compare(lexems, lines):
    for line in lines:
        for lexeme in line.split():
            if lexeme in lexems:
                return True

    return False


def identify_lang(lexems, lines):
    for lang in lexems:
        asserted = compare(lexems[lang], lines)

        if asserted:
            return lang

    return


def get_input():
    rows = int(input('Введите кол-во строк: '))

    return [input('#> ') for _ in range(rows)]


lexems = {
    'xml': ['CDATA', '<?xml version="1.0" encoding="utf-8"?>', '?xml'],
    'html': ['<!doctype html>', '<html>', '<body>', '<head>', '<meta>'],
    'json': ['{', '}', ':']
}

lines = get_input()

identified_lang = identify_lang(lexems, lines)

print('It hasn\t been determined' if not identified_lang else f'That was {identified_lang}')
