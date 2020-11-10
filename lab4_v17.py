from typing import List


def get_col_input(length: int) -> List[int]:
    accumulator: List[int] = []

    for j in range(length):
        accumulator.append(int(input(f'\tCol {j + 1} > ')))

    return accumulator


def print_prelude(prelude: str, splitter_count: int = 20, splitter: str = '-'):
    print(f'\n{prelude}')
    print(splitter * splitter_count)


matrix: List[List[int]] = []

rows: int = int(input('Enter rows count: '))
cols: int = int(input('Enter columns count: '))
insertion_index: int = int(input('Enter an insertion index: '))

for i in range(rows):
    print_prelude(f'Row {i + 1}')
    matrix.append(get_col_input(cols))

print_prelude('An insertion row')

insertion_row: List[int] = get_col_input(cols)
result: List[List[int]] = matrix[:insertion_index] + [insertion_row] + matrix[insertion_index:]

print_prelude('Result', splitter='+')

for row in result:
    print(row)
