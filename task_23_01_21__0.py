def sort_list(iterable, descending=False):
    sorted_list = iterable.copy()

    for i, item in enumerate(sorted_list):
        for j in range(i + 1, len(sorted_list)):
            if (not descending and item > sorted_list[j]) or (descending and item < sorted_list[j]):
                sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]

    return sorted_list


def take_around(iterable):
    min_value = max_value = None
    max_idx = min_idx = 0

    for idx, item in enumerate(iterable):
        if (min_value is None) or (item < min_value):
            min_value = item
            min_idx = idx

        if (max_value is None) or (item > max_value):
            max_value = item
            max_idx = idx

    if min_idx > max_idx:
        return []

    taken = []

    for idx, item in enumerate(iterable):
        if not min_idx <= idx <= max_idx:
            taken.append(item)

    return taken


values = [45, 2, 11, 44, 69, 228, 20, 23, 5]
ordered = take_around(values)

print(ordered)
