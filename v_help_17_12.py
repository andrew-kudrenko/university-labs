user_string = input('Введите строку: ')
user_word = input('Введите слово: ')

vowels = 'ёуеыаоэяию'
intersections = ''

for letter in vowels:
    lowed = letter.lower()
    if (lowed in user_string) and (lowed in user_word):
        intersections += letter

print(intersections)
