n = int(input("Введите кол-во строк: "))
m = int(input("Введите кол-во столбцов: "))

r = f = d = t = 0

a = [[0] * (m + 1) for i in range(n + 1)]

for i in range(n):
    for j in range(m):
        k = int(input("Введите число: "))
        a[i][j] = k

for row in a:
    c = sum(row) / n
    row[m] = c

# while t != m:
#     while r != n:
#         c = a[r][f]
#         d += c
#         r += 1
#         d = d / m
#         a[-1].append(d)
#         r = 0
#         f += 1
#         t += 1
#         d = 0
#         c = 0

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
