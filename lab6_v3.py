def get_input():
    dict_lines_number = int(input('Enter dict lines count: '))
    data_lines_number = int(input('Enter data lines count: '))

    data_lines = []
    dict_lines = []

    print('Dict input. Don\t forget about commas! Input format [Country]: City0, City1, CityN')
    for i in range(dict_lines_number):
        dict_lines.append(input('> '))

    print('Data input. Input format [City]')
    for i in range(data_lines_number):
        data_lines.append(input('> '))

    return dict_lines, data_lines


def create_dict(lines, key_splitter=':', values_splitter=','):
    accumulator = {}

    for line in lines:
        key = line.split(key_splitter)[0]
        values = list(map(lambda s: s.strip(), line.split(key_splitter)[1].split(values_splitter)))

        accumulator[key] = values

    return accumulator


def match_city(city, countries):
    for key in countries:
        if city in countries[key]:
            return f'{city} in {key}'

    return 'Not found'


countries, cities = get_input()
countries = create_dict(countries)

for city in cities:
    print(match_city(city, countries))
