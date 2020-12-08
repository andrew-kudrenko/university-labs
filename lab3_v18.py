string: str = input('Enter a string: ')
substring: str = input('Enter the substring: ')
new_substring: str = input('Enter a new substring: ')

matched: bool = False

word_start: int = 0
word_end: int = 0

result: str = ''

i: int = 0

while i < len(string):
    word_start = i

    for j in range(len(substring)):
        if string[i + j] != substring[j]:
            matched = False
            break

        if j == len(substring) - 1:
            matched = True
            word_end = j + i

    if matched:
        i = word_end + 1
        result += new_substring
    else:
        result += string[i]
        i += 1

print(f'Edited string: {result}')
