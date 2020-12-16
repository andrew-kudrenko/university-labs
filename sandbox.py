import numpy as np


def take_above(matrix, side=False):
    taken = []

    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if (not side and (x > y)) or (side and (x < len(matrix) - y - 1)):
                taken.append(matrix[y][x])

    return taken


def add_above_main(matrix):
    sum = 0

    for item in take_above(matrix):
        sum += item

    return sum


print('Size of matrix')

rows = int(input('Rows = '))
cols = int(input('Cols = '))

matrix = np.random.randint(1, 10, (rows, cols))

print('Initial matrix\n', matrix)
print(f'Summary equals {add_above_main(matrix)}')
