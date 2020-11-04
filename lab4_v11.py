from typing import List, TypeVar, Union

T = TypeVar('T')


def sort_list(iterable: List[T], descending: bool = False) -> List[T]:
    sorted_list: List[T] = iterable.copy()

    for i, item in enumerate(sorted_list):
        for j in range(i + 1, len(sorted_list)):
            if (not descending and item > sorted_list[j]) or (descending and item < sorted_list[j]):
                sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]

    return sorted_list


def remove_divides_by_two(iterable: List[Union[int, float]]) -> List[Union[int, float]]:
    filtered: List[Union[int, float]] = []

    for item in iterable:
        if item % 2 == 0:
            filtered.append(item)

    return filtered


# numbers = [i for i in range(10)]
numbers = list(map(int, input('Enter a sequence of numbers: ').split()))

print(sort_list(remove_divides_by_two(numbers)))
