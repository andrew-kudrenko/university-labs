def compare(dist_signs, rows):
    for row in rows:
        for lexeme in row.split():
            if lexeme in dist_signs:
                return True

    return False


def determine_lang(dist_signs, rows):
    for lang in dist_signs:
        found = compare(dist_signs[lang], rows)

        if found:
            return lang

    return None


def get_lines():
    rows = int(input('Rows count: '))

    return [input('> ') for _ in range(rows)]


dist_signs = {
    'c++': ['using', '#include', 'namespace', 'std::cout', 'std::cin', 'std::endl'],
    'python': ['def', 'in range', 'except', 'lambda'],
    'pascal': [':=', '<>', 'begin', 'end.', 'end', 'Writeln', 'Readln', 'Read', 'Write', 'Randomize']
}

lines = get_lines()

determined = determine_lang(dist_signs, lines)

print('Undefined' if not determined else determined)
