import numpy as np


def find_max_col(row):
    max_value = row[0]

    for col in row:
        if col > max_value:
            max_value = col

    return max_value


def divide_row(row, divider):
    return [col / divider for col in row]


def print_matrix(matrix):
    for row in matrix:
        print(row)

    print('\n')


print('Enter a size')

rows = int(input('Rows = '))
cols = int(input('Cols = '))

matrix = np.random.rand(rows, cols)
calculated = []

for row in matrix:
    max_col = find_max_col(row)
    calculated.append(divide_row(row, max_col))

print('Initial matrix')
print_matrix(matrix)

print('Calculated matrix')
print_matrix(calculated)
