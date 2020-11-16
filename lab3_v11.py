input_data: str = input('Введите строку: ')
need_length: int = int(input('Выберите требуемую длину: '))

letters_counter: int = 0
words_counter: int = 0

prev_symbol: str = ' '

for i, symbol in enumerate(input_data):
    if symbol != ' ':
        letters_counter += 1

    if symbol == ' ' and prev_symbol != ' ' or symbol != ' ' and i == len(input_data) - 1:
        words_counter += 1

    prev_symbol = symbol

if letters_counter == 0:
    print('Не найдено ни одного слова')
elif need_length < len(input_data):
    print('Требуемая длина не должна быть меньше исходной')
elif words_counter <= 1:
    print(input_data)
else:
    whitespaces_per_word: int = need_length // (words_counter - 1)
    whitespaces_rest: int = need_length % (words_counter - 1)

    concatenated: str = ''

    prev_symbol = ''
    words_counter = 0
    replaced_whitespace_index: int = 0

    for i, symbol in enumerate(input_data):
        if symbol == ' ' and prev_symbol != ' ' or symbol != ' ' and i == len(input_data) - 1:
            words_counter += 1

        if symbol != ' ':
            concatenated += symbol
        elif replaced_whitespace_index == 0 and words_counter == 1:
            concatenated += ' ' * whitespaces_per_word + ' ' * whitespaces_rest
        elif replaced_whitespace_index != i:
            replaced_whitespace_index = i
            concatenated += ' ' * whitespaces_per_word
            replaced_whitespace_index = i

        prev_symbol = symbol

    print(concatenated)
