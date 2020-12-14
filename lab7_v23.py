def starts_from_upper(word): return word[0].lower() == word[0]


def capitalize(word): return word[0].upper() + word[1:]


def fix_register(line):
    words = line.split()

    for idx, word in enumerate(words):
        if starts_from_upper(word):
            words[idx] = capitalize(word)

    return ' '.join(words)


def handle_file(in_filename, out_filename):
    in_file = open(in_filename, 'r', encoding='utf-8')
    out_file = open(out_filename, 'w', encoding='utf-8')

    for row in in_file:
        out_file.writelines(fix_register(row) + '\n')

    in_file.close()
    out_file.close()


handle_file('lab7_v23_input.txt', 'lab7_v23_output.txt')
