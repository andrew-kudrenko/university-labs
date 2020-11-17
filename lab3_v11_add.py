from typing import List

letters: List[str] = input('Enter a sequence of letters: ').split()

for i in range(len(letters) - 1):
    for j in range(len(letters) - 1 - i):
        if letters[j + 1] < letters[j]:
            letters[j + 1], letters[j] = letters[j], letters[j + 1]

ordered: List[str] = []
duplicates: List[str] = []

for letter in letters:
    intersections: int = 0

    for _, shifted_letter in enumerate(letters):
        if shifted_letter == letter:
            intersections += 1

    if intersections > 1 and letter not in duplicates:
        duplicates.append(letter)

    if letter not in ordered:
        ordered.append(letter)

print(f'Ordered list: {ordered}')
print(f'Duplicates: {duplicates}')
