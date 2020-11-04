from typing import List, TypeVar, Union

T = TypeVar('T')


def sort_list(iterable: List[T], descending: bool = False) -> List[T]:
    sorted_list: List[T] = iterable.copy()

    for i, item in enumerate(sorted_list):
        for j in range(i + 1, len(sorted_list)):
            if (not descending and item > sorted_list[j]) or (descending and item < sorted_list[j]):
                sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]

    return sorted_list


def separate_list_by_sign(iterable: List[T], by_positive: bool = False) -> List[T]:
    separated_list: List[T] = []

    for item in iterable:
        if (by_positive and item >= 0) or (not by_positive and item < 0):
            separated_list.append(item)

    return separated_list


# numbers = [i for i in range(-5, 5)]
numbers = list(map(int, input('Enter a sequence of numbers: ').split()))

result = sort_list(separate_list_by_sign(numbers), True) + sort_list(separate_list_by_sign(numbers, by_positive=True))

print(result)
