def read_lines(filename):
    file = open(filename)
    symbols = file.read()
    file.close()

    return symbols


def filter_duplicates(iterable):
    filtered = []

    for symbol in iterable:
        if symbol not in filtered:
            filtered.append(symbol)

    return filtered


def reverse_list(iterable):
    return [iterable[i] for i in range(len(iterable) - 1, -1, -1)]


def write_result(filename, sequence):
    file = open(filename, mode='w', encoding="utf-8")

    for symbol in sequence:
        file.write(symbol)

    file.close()


write_result('lab7_v12_result.txt', reverse_list(filter_duplicates(read_lines('lab7_v12_input.txt'))))
