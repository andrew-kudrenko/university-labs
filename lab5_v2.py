import numpy as np


def calc_max_average(matrix): return np.max([np.mean(row) for row in matrix])


def generate_matrix(start, stop, prelude):
    print(prelude)

    rows = int(input('Rows = '))
    cols = int(input('Cols = '))

    return np.random.randint(start, stop, (rows, cols))


matrix = generate_matrix(1, 10, 'Matrix')
print(f'Initial matrix\n{matrix}\nAverage equals {calc_max_average(matrix)}')
