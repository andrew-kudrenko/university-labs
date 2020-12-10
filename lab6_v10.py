def create_dict(lines):
    total = {}

    for line in lines:
        key, value = line.split(':')
        total[key.strip()] = [int(value)]

    return total


def find_max_amount(data):
    max_amount = None, None

    for key in data:
        if not max_amount[1] or data[key] > max_amount[1]:
            max_amount = key, data[key]

    return max_amount[0]


print('Expect data in format [Name]: Amount')

current_row = ''
lines = []

while current_row.strip() != '0':
    if current_row:
        lines.append(current_row)

    current_row = input('> ')

print(find_max_amount(create_dict(lines)))
