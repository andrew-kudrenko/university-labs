input_data: str = input('Enter words: ')

prev_symbol: str = ''
word_start: int = 0
word_end: int = 0

words_without_duplicates: str = ''

for symbol_idx, symbol in enumerate(input_data):
    if prev_symbol == ' ' and symbol != ' ':
        word_start = symbol_idx

    if prev_symbol != ' ' and symbol == ' ' or symbol != ' ' and len(input_data) - 1 == symbol_idx:
        word_end = symbol_idx

        has_duplicates: bool = False
        current_word: str = ''

        for i in range(word_start, word_end + 1):
            if input_data[i] in current_word:
                has_duplicates = True
                break

            current_word += input_data[i]

        if not has_duplicates:
            words_without_duplicates += current_word + ' '

    prev_symbol = symbol

print(words_without_duplicates)
