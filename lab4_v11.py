from typing import List, TypeVar, Union

T = TypeVar('T')


def needs_for_swap(a: T, b: T, descending: bool) -> bool:
    return (not descending and a > b) or (descending and a < b)


def sort_list(iterable: List[T], descending: bool = False) -> List[T]:
    sorted_list: List[T] = iterable.copy()

    for i in range(len(sorted_list) - 1):
        for j in range(len(sorted_list) - i - 1):
            if needs_for_swap(sorted_list[j], sorted_list[j + 1], descending):
                sorted_list[j + 1], sorted_list[j] = sorted_list[j], sorted_list[j + 1]

    return sorted_list


def remove_divides_by_two(iterable: List[Union[int, float]]) -> List[Union[int, float]]:
    filtered: List[Union[int, float]] = []

    for item in iterable:
        if item % 2 != 0:
            filtered.append(item)

    return filtered


# numbers = [i for i in range(10)]
numbers = list(map(int, input('Enter a sequence of numbers: ').split()))

print(f'Sorted: {sort_list(remove_divides_by_two(numbers))}')
