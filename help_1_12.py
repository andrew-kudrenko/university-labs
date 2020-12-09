def find_min(file):
    min_length = min_index = -1

    for i, row in enumerate(file):
        if len(row) < min_length or min_index == -1:
            min_length = len(row)
            min_index = i

    return min_length, min_index


def write_reverse(file, lines):
    for i, row in enumerate(lines):
        file.write(lines[len(lines) - i - 1])


file = open("assets/star_named_sun.txt", encoding="utf-8")
file2 = open("assets/result.txt", "w", encoding="utf-8")

min_length, min_index = find_min(file)

file.seek(0)
lines = file.readlines()

min_row = lines[min_index]

file2.write(min_row)
write_reverse(file2, lines)

file2.writelines(min_row)

file2.close()
file.close()
