from typing import List
import numpy as np


def print_matrix(iterable: List[List[any]]) -> None:
    for r in iterable:
        print('|'.join(list(map(lambda c: f'{c}'.ljust(25), r))))


def create_matrix(rows: int, cols: int) -> List[List[float]]:
    return np.random.rand(rows, cols)


def handle_matrix(matrix: List[List[float]], target_index: int) -> List[List[float]]:
    target: List[float] = matrix[target_index]
    changed: List[List[float]] = matrix.copy()

    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            changed[i][j] += target[j]

    return changed


print('Enter a size')

rows: int = int(input('Rows = '))
cols: int = int(input('Cols = '))

print('Enter a target row')

target_index: int = int(input('Target row = '))
matrix: List[List[float]] = create_matrix(rows, cols)

print_matrix(matrix)
print('*' * 50)
print_matrix(handle_matrix(matrix, target_index))
