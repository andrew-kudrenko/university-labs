file = open('assets/star_named_sun.txt')

min_length = min_index = -1

for i, row in enumerate(file):
    if len(row) < min_length or min_index == -1:
        min_length = len(row)
        min_index = i


print(f'Minimal length equals {min_length} Found by index {min_index}')

file.close()
