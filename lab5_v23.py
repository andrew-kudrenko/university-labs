import numpy as np


def take(matrix, side=False, below=False):
    taken = []

    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            computed = len(matrix) - y - 1

            if (not side and (x < y if below else x > y)) or (side and (x > computed if below else x < computed)):
                taken.append(matrix[y][x])

    return taken


def add(matrix, side=False, below=False):
    sum = 0

    for item in take(matrix, side, below):
        sum += item

    return sum


def mult(matrix, side=False, below=False):
    product = 1

    for item in take(matrix, side, below):
        product *= item

    return product


print('Size of matrix')

rows = int(input('Rows = '))
cols = int(input('Cols = '))

matrix = np.random.randint(1, 10, (rows, cols))

print('Initial matrix\n', matrix)
print(f'Summary below main equals {add(matrix, below=True)}\nSummary above side equals {add(matrix, side=True)}')
