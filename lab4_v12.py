from typing import List


def custom_sorted(iterable: List[int]) -> List[int]:
    even: List[int] = sorted(iterable[::2], reverse=True)
    odd: List[int] = sorted(iterable[1::2])

    return [even[i // 2] if i % 2 == 0 else odd[i // 2] for i in range(len(iterable))]


# numbers = [i for i in range(6)]
numbers: List[int] = list(map(int, input('Enter a sequence of integers: ').split()))

print(custom_sorted(numbers))
