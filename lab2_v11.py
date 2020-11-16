max_value: int = 0
max_index: int = 0
index: int = 0
current: int = -1

print('Enter an integer')

while current != 0:
    current = int(input('> '))

    if current > max_value:
        max_value = current
        max_index = index

    index += 1

print(f'Max value equals {max_value}\nFound by index {max_index}')
