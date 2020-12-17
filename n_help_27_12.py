def to_dict(lines):
    total = {}

    for line in lines:
        if line.strip() == '0':
            break

        key = line.split(':')[0]

        if key not in total:
            total[key] = []

            for current in lines:
                current_key = current.split(':')[0]

                if key == current_key:
                    profit, outlay, year = current.split(':')[1].split()
                    total[key].append({'year': int(year), 'profit': int(profit), 'outlay': int(outlay)})

    return total


def unprofitable(data):
    result = (None, None, None)

    for city in data:
        for current in data[city]:
            diff = current['profit'] - current['outlay']

            if not result[2] or (diff < result[2]):
                result = city, current['year'], diff

    return result


# lines = [
#     'A: 1000 890 2001',
#     'C: 800 1200 1999',
#     'B: 900 900 2000',
#     'B: 750 900 2007',
#     'C: 850 1000 2004',
#     'A: 1500 450 1998',
#     '0'
# ]

print('Enter data in format [City]: [Profit] [Outlay] [Year]')

lines = []
input_has_ended = False

while not input_has_ended:
    current = input('> ')

    if current.strip() == '0':
        input_has_ended = True
    else:
        lines.append(current)

city, year, lost = unprofitable(to_dict(lines))

print(f'The most unprofitable year for city {city} was {year}. {abs(lost)}$ lost')
