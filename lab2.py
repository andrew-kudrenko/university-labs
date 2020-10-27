from typing import Optional


print('Enter a sequence of numbers. Script will find max value until 0 will be entered')

number: Optional[int] = None
current_index: int = 0

max_value: Optional[int] = None
max_value_index: Optional[int] = None

while number != 0:
    number = int(input('> '))

    if not max_value or number > max_value:
        max_value = number
        max_value_index = current_index

if max_value:
    print(f'Max value by index {max_value_index} equals {max_value}')
else:
    print('Incorrect input')
