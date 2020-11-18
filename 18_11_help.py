def get_vowels():
    return 'aeiouy'


def includes(letter, sequence):
    for word in sequence:
        if letter.lower() not in word:
            return False

    return True


def separate_included(sequence):
    ordered_letters = {}

    for letter in get_vowels():
        ordered_letters[letter] = includes(letter, sequence)

    return ordered_letters


def print_found(separated):
    result = ''

    for key in separated.keys():
        if separated[key]:
            result += key

    print(result)


print('Enter a word\'s sequence, separated by comma. Terminate by dot')
words = input('> ').split('.')[0].split(',')

print_found(separate_included(words))
