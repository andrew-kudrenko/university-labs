import numpy as np


def handle_matrix(matrix, target):
    handled = matrix.copy()

    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            handled[y][x] *= matrix[y][target]

    return handled


rows = int(input('Rows number\n> '))
cols = int(input('Cols number\n> '))

target = int(input('Target index\n> '))

matrix = np.random.randint(0, 10, (rows, cols))

print('Initial matrix\n', matrix)
print('Handled matrix\n', handle_matrix(matrix, target))
