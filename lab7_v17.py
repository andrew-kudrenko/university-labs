def find_repeats_for(count, lines):
    repeats = {}

    for line in lines:
        for word in line.split():
            repeats[word] = 1 if word not in repeats else repeats[word] + 1

    found = []

    for key in repeats:
        if repeats[key] >= count:
            found.append(key)

    return found


def filter_repeats(repeats, lines):
    filtered = []

    for line in lines:
        filtered_line = []

        for word in line.split():
            if word not in repeats:
                filtered_line.append(word)

        filtered.append(' '.join(filtered_line))

    return filtered


def handle_files(repeats_count, input_filename, out_filename):
    log = f'File has no rows with {repeats_count} repeats'

    with open(input_filename) as input_file:
        lines = input_file.readlines()
        repeats = find_repeats_for(repeats_count, lines)

        with open(out_filename, 'w') as out_file:
            out_file.writelines('\n'.join(filter_repeats(repeats, lines)))

            if not repeats:
                print(log)
                out_file.write(log)


handle_files(2, 'lab7_v17_input.txt', 'lab7_output.txt')
