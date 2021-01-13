def do_task(collection):
    great_than_null = []

    if includes_negative(collection):
        min_item = None
        max_item = None
        min_pos = max_pos = None

        for i, item in enumerate(collection):
            if (min_item is None) or (item < min_item):
                min_item = item
                min_pos = i

            if (max_item is None) or (item > max_item):
                max_item = item
                max_pos = i

        for i in range(min_pos + 1, max_pos):
            if collection[i] > 0:
                great_than_null.append(collection[i])

        for i in range(len(great_than_null) - 1):
            for j in range(len(great_than_null) - i - 1):
                if great_than_null[j] < great_than_null[j + 1]:
                    great_than_null[j + 1], great_than_null[j] = great_than_null[j], great_than_null[j + 1]

        return great_than_null
    else:
        return []


def includes_negative(collection):
    for item in collection:
        if item < 0:
            return True

    return False


file = open('dmitry_exam_output.txt', mode='w', encoding='utf-8')

print('Enter a sequence')

gotten_input = [int(n) for n in input('> ').split()]
task_result = do_task(gotten_input)

print(f'The sequence has {len(task_result)} elements')
print(str(task_result))

file.write(str(task_result))
file.close()

# 4 -3 11 9 32 6 77 69 1 228 3