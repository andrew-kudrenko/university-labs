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


whitespaces_per_word: int = (need_length - letters_counter) // (words_counter - 1)
whitespaces_rest: int = (need_length - letters_counter) % (words_counter - 1)

concatenated: str = ''

prev_symbol = ''
current_word = 0

for i, symbol in enumerate(input_data):
    if symbol == ' ' and prev_symbol != ' ' or symbol != ' ' and i == len(input_data) - 1:
        current_word += 1

    if symbol != ' ':
        concatenated += symbol
    elif current_word == words_counter - 1:
        concatenated += ' ' * (whitespaces_per_word + whitespaces_rest)
    else:
        concatenated += ' ' * whitespaces_per_word

    prev_symbol = symbol

print(concatenated)
