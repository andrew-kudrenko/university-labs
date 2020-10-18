from typing import List

input_data: str = input('Enter a string: ')
words: List[str] = input_data.split()
need_length: int = int(input('Enter length, which the string should have: '))
current_length: int = 0

for word in words:
    current_length += len(word)

need_whitespaces: int = need_length - current_length

if need_length - len(input_data) < 0:
    print('Incorrect value. Need length less than initial')
else:
    whitespaces_per_word: int = need_whitespaces // (len(words) - 1)
    whitespaces_rest: int = need_whitespaces % (len(words) - 1)

    list_header: str = words[0]
    list_body: List[str] = words[1::]

    splitter: str = ' '
    splitter_group: str = splitter * whitespaces_per_word
    splitter_rest_group: str = splitter * whitespaces_rest

    combined: str = list_header + (splitter_group + splitter_rest_group) + splitter_group.join(list_body)

    print(combined)
