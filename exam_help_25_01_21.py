def is_ordered(iterable):
    ascending = descending = False

    for i in range(1, len(iterable)):
        if ascending == descending:
            if iterable[i] > iterable[i - 1]:
                ascending = True
            else:
                descending = True

        if (ascending and (iterable[i] < iterable[i - 1])) or (descending and (iterable[i] > iterable[i - 1])):
            return False

    return True


def save_result(filename, iterable):
    file = open(filename, 'w', encoding='utf-8')

    message = f'The array has{"" if is_ordered(iterable) else " not"} been sorted'
    file.write(message)

    file.close()


data = [9, 32, 76, 228, 1337, 19]

save_result('exam_25_01_21.txt', data)
