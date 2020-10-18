from typing import List, Optional


numbers: List[int] = map(int, input('Enter a sequence of integers: ').split())

max_value: Optional[int] = None
max_value_index: Optional[int] = None

for idx, number in enumerate(numbers):
    if not max_value or number > max_value:
        max_value = number
        max_value_index = idx

if max_value:
    print(f'Max value by index {max_value_index} equals {max_value}')
else:
    print('Incorrect input')
