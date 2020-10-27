from typing import List


numbers: List[int] = list(map(int, input('Enter an array: ').split()))
duplicates: List[int] = []

for number in numbers:
    entrance_counter: int = 0

    for nested_number in numbers:
        if nested_number == number:
            entrance_counter += 1

    if entrance_counter > 2 and number not in duplicates:
        duplicates.append(number)

for i in range(len(duplicates)):
    for j in range(i + 1, len(duplicates)):
        if duplicates[i] > duplicates[j]:
            duplicates[i], duplicates[j] = duplicates[j], duplicates[i]

if duplicates:
    print(f'Sorted array of duplicates: {duplicates}')
else:
    print('Array has no duplicates')
