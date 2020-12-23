from typing import List


def even(sequence: List[int]) -> List[int]:
    extracted: List[int] = []

    for idx, num in enumerate(sequence):
        if idx % 2 == 0:
            extracted.append(num)

    return extracted


def repeats_for(sequence: List[int], count: int = 2) -> List[int]:
    duplicates = []
    matched = {}

    for num in sequence:
        if num not in matched:
            matched[num] = 1
        else:
            matched[num] += 1

    for key in matched:
        if matched[key] > count:
            duplicates.append(key)

    return duplicates


def order(sequence: List[int]) -> List[int]:
    ordered = sequence.copy()

    for i in range(len(ordered) - 1):
        for j in range(len(ordered) - i - 1):
            if ordered[j] > ordered[j + 1]:
                ordered[j + 1], ordered[j] = ordered[j], ordered[j + 1]

    return ordered


numbers: List[int] = [9, -3, 4, 5, 11, 4, -3, 9, 11, 8, 4, -3, 11, 9, 9, 9, 4, 4, 5, 5, 9, 4]

file = open('my_exam_output.txt', 'w', encoding='utf-8')

file.write(str(order(repeats_for(even(numbers), 2))))

file.close()
