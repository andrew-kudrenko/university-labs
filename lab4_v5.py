from typing import List

# matrix = [[2, 2, 3], [3, 4, 5], [6, 7, 8]]

matrix: List[List[float]] = []

rows: int = int(input('Enter rows count: '))
cols: int = int(input('Enter columns count: '))

for i in range(rows):
    print(f'Row {i + 1}')
    print('-' * 20)
    matrix.append([])

    for j in range(cols):
        matrix[i].append(float(input(f'Col {j + 1} > ')))


result: List[List[float]] = [*[[*[item for item in row], 0] for row in matrix], [0] * (cols + 1)]

for i in range(rows):
    row_sum: float = 0
    col_sum: float = 0

    for j in range(cols):
        row_sum += result[i][j]
        col_sum += result[j][i]

    result[i][cols] = row_sum / cols
    result[rows][i] = col_sum / rows

print('-' * 20)

for row in result:
    print(list(map(lambda col: f'{round(col, 2)}'.ljust(4), row)))