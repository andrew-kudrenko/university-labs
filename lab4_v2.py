def bubble_sort(iterable):
    handled = iterable.copy()

    for i in range(len(handled)):
        for j in range(len(handled) - 1):
            if handled[j] > handled[j + 1]:
                handled[j], handled[j + 1] = handled[j + 1], handled[j]

    return handled


def extract_unique(iterable):
    unique = []

    for item in iterable:
        inclusions = 0

        for deep_item in iterable:
            if deep_item == item:
                inclusions += 1

        if inclusions < 2:
            unique.append(item)

    return unique


sequence = [int(item) for item in input('Enter an integers sequence: ').split()]
print(f'Result: {bubble_sort(extract_unique(sequence))}')
