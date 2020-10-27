words: str = input('Enter words, separated by comma: ')

separator: str = ','
words_through_whitespaces: str = ''

words_counter: int = 0
prev_symbol: str = ' '

word_start: int = 0
word_end: int = 0

for i, symbol in enumerate(words):
    if (prev_symbol == separator or prev_symbol == ' ') and symbol != separator and symbol != ' ':
        word_start = i

    if prev_symbol != ' ' and prev_symbol != separator and (symbol == separator or symbol == ' ') or \
       symbol != ' ' and symbol != separator and i == len(words) - 1:
        words_counter += 1
        word_end = i

        if i == len(words) - 1:
            word_end += 1

        for j in range(word_start, word_end + 0):
            words_through_whitespaces += words[j]

        words_through_whitespaces += ' '

    prev_symbol = symbol

shuffled_words: str = ''

prev_word: str = ''
current_word: str = ''

prev_symbol = ' '

words_counter = 0
word_start = 0
word_end = 0

for i, symbol in enumerate(words_through_whitespaces):
    if prev_symbol == ' ' and symbol != ' ':
        word_start = i

    if prev_symbol != ' ' and symbol == ' ' or symbol != ' ' and i == len(words_through_whitespaces) - 1:
        words_counter += 1
        word_end = i

        if i == len(words) - 1:
            word_end += 1

        prev_word = current_word
        current_word = ''

        for j in range(word_start, word_end):
            current_word += words_through_whitespaces[j]

        if words_counter % 2 == 0:
            shuffled_words += ' ' + current_word + ' ' + prev_word
        elif i == len(words_through_whitespaces) - 1:
            shuffled_words += ' ' + current_word

    prev_symbol = symbol

print(shuffled_words)
