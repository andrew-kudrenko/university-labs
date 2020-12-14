def find_the_longest(lines):
    found = ''

    for line in lines:
        if len(found) < len(line):
            found = line

    return found.strip()


def handle_file(filename, comparable):
    file = open(filename, 'r+', encoding='utf-8')
    longest = find_the_longest(file.readlines())

    if longest != comparable:
        file.write(longest)

    file.close()


handle_file('lab7_v2_input.txt', input('Enter any phrase: '))
