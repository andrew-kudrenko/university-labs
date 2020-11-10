n = int(input("Введите кол-во строк: "))
m = int(input("Введите кол-во столбцов: "))

a = [[0] * (m + 1) for i in range(n + 1)]

for i in range(n):
    for j in range(m):
        k = int(input("Введите число: "))
        a[i][j] = k

for row in a:
    c = sum(row) / n
    row[m] = c

for i in range(m):
    sum_of_col = 0

    for j in range(n):
        sum_of_col += a[j][i]

    a[n][i] = sum_of_col / n

for row in a:
    formatted_row = ''

    for col in row:
        formatted_row += f'{col}'.ljust(5)

    print(formatted_row)
