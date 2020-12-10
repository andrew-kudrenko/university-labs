def read_matrixes(filename):
    matrixes = []
    current = []

    file = open(filename, 'r', encoding='utf-8')

    for row in file:
        if row.strip() == '' and current:
            matrixes.append(current)
            current = []
        elif row.strip() != '':
            current.append([int(item) for item in row.split()])

    matrixes.append(current)
    file.close()

    return matrixes


def delete_side_diagonal(matrix):
    handled = []

    for y in range(len(matrix)):
        row = []
        for x in range(len(matrix[y])):
            if x != len(matrix) - y - 1:
                row.append(matrix[y][x])

        handled.append(row)

    return handled


def write_handled(matrixes, callback, filename):
    file = open(filename, 'w', encoding='utf-8')

    for matrix in matrixes:
        for row in callback(matrix):
            file.write(f'{" ".join([str(item) for item in row])}\n')

        file.write('\n')

    file.close


write_handled(read_matrixes('lab7_v10_input.txt'), delete_side_diagonal, 'lab7_v10_output.txt')
