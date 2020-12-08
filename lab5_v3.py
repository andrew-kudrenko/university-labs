import numpy as np


def print_matrix(iterable):
    for r in iterable:
        print('|'.join(list(map(lambda c: f'{c}'.ljust(25), r))))


def create_matrix(rows, cols):
    return np.random.rand(rows, cols)


def find_col(matrix):
    min_value = None, None

    for x in range(len(matrix[0])):
        sum_of_col = 0

        for y in range(len(matrix)):
            sum_of_col += matrix[y][x]

        if not min_value[1] or min_value[1] > sum_of_col:
            min_value = x, sum_of_col

    return min_value[0]


def find_min_from_col(matrix, col_idx):
    min_value = None

    for y in range(len(matrix)):
        current = matrix[y][col_idx]

        if not min_value or min_value > current:
            min_value = current

    return min_value


print('Enter a size')

rows = int(input('Rows = '))
cols = int(input('Cols = '))

matrix = create_matrix(rows, cols)

print('Matrix')
print_matrix(matrix)

print('-' * 69)

print(f'Found item is {find_min_from_col(matrix, find_col(matrix))}')
