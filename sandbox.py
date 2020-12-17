def filter_even(numbers):
    filtered = []

    for number in numbers:
        if number % 2 != 0:
            filtered.append(number)

    return numbers


numbers = [int(item) for item in input('Введите числа: ').split()]
print('Обработанный список', sorted(filter_even(numbers)))


# Назначение: Отлильтровать список от четных элементов
# Параметры:
#   numbers - список чисел для фильтрации
# Возвращаемое значение: Новый список чисел без четных элементов
