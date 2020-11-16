from typing import List
import numpy as np


def print_matrix(iterable: List[List[any]]) -> None:
    for r in iterable:
        print(list(map(lambda c: f'{c}'.ljust(20), r)))


print('Enter a size')

rows: int = int(input('Rows = '))
cols: int = int(input('Cols = '))

print('Enter a target row')

target_index: int = int(input('Target row = '))
matrix: List[List[float]] = np.random.rand(rows, cols)

target: List[float] = matrix[target_index]
changed: List[List[float]] = matrix.copy()

for i, row in enumerate(matrix):
    for j, col in enumerate(row):
        changed[i][j] += target[j]

print_matrix(matrix)
print('*' * 50)
print_matrix(changed)
