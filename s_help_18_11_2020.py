from random import randint


def print_matrix(matrix, padding=5):
    for row in matrix:
        print(' '.join(list(map(lambda col: f'| {col}'.ljust(padding), row))), '|\n')


def invert_tuple(pair):
    return pair[1], pair[0]


def create_with_random(rows, cols, top, bottom=0):
    return [[randint(bottom, top) for col in range(cols)] for row in range(rows)]


def reflect_triangle(triangle):
    reflected = []

    for group in triangle:
        reflected.append(list(map(lambda t: invert_tuple(t), group)))

    return reflected


def get_diagonal_indices(matrix):
    indices = []

    rows = len(matrix)
    cols = len(matrix[0])

    for row in range(rows - 1, -1, -1):
        group = []

        for col in range(cols - row):
            group.append((col, row + col))

        indices.append(group)

    indices += reversed(reflect_triangle(indices[:-1]))

    return indices


def exclude_main_diagonal(diagonals):
    filtered = []
    max_length = 0

    for diagonal in diagonals:
        if len(diagonal) > max_length:
            max_length = len(diagonal)

    for diagonal in diagonals:
        if len(diagonal) != max_length:
            filtered.append(diagonal)

    return filtered


def calc_sum(matrix, indices):
    diagonals_sum = []

    for pairs in indices:
        group_sum = 0

        for x, y in pairs:
            group_sum += matrix[y][x]

        diagonals_sum.append(group_sum)

    return diagonals_sum


matrix = create_with_random(5, 5, 10, 0)

print_matrix(matrix, 7)

print('-' * 40)

print(calc_sum(matrix, exclude_main_diagonal(get_diagonal_indices(matrix))))
