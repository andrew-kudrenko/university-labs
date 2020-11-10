row = int(input('Введите количество строк: '))
column = int(input('Введите количество столбцов: '))
place = int(input('Введите номер строки, куда нужно будет вставить новую: '))

matrix = []
str_add = []

for i in range(row):
    matrix.append([])
    for j in range(column):
        matrix[i].append(int(input('Введите элемент строки: ')))

print('Введите строку для вставки')
for i in range(column):
    str_add.append(int(input('Введите элемент строки: ')))

array_two = []

i = 0
while i < row:
    if i == place:
        array_two.append(str_add)

    array_two.append(matrix[i])
    i += 1

print(array_two)
