def check_for_intersections(a, b):
    vowels = 'ёуеыаоэяию'
    intersections = ''

    for letter in vowels:
        lowed = letter.lower()
        if (lowed in a) and (lowed in b):
            intersections += letter

    return intersections


user_string = input('Введите строку: ')
user_word = input('Введите слово: ')

print(check_for_intersections(user_string, user_word))
