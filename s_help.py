def fill_matrix(matrix, rows, cols):
    print('Enter a matrix')

    for row in range(rows):
        print()
        for col in range(cols):
            matrix[row][col] = int(input('> '))


rows = int(input('Rows: '))
cols = int(input('Cols: '))

a = [[0] * cols for row in range(rows)]

fill_matrix(a, rows, cols)

max_sum = 0

for col in range(cols):
    sum_of_col = 0

    for row in range(rows):
        sum_of_col += a[row][col]

    if sum_of_col > max_sum:
        max_sum = sum_of_col

print(f'Max sum equals {max_sum}')
