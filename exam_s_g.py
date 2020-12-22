def has_negative(arr):
    for num in arr:
        if num < 0:
            return True

    return False


def handle(arr):
    if not has_negative(arr):
        return []

    negative = []
    min_value = max_value = None
    min_index = max_index = None

    for idx, num in enumerate(arr):
        if (not min_value) or (num < min_value):
            min_value = num
            min_index = idx

        if (not max_value) or (num > max_value):
            max_value = num
            max_index = idx

    for i in range(min_index + 1, max_index):
        if arr[i] < 0:
            negative.append(arr[i])

    for i in range(len(negative) - 1):
        for j in range(len(negative) - i - 1):
            if negative[j] < negative[j + 1]:
                negative[j + 1], negative[j] = negative[j], negative[j + 1]

    return negative


file = open('out.txt')

file.write(str(handle([int(n) for n in input('> ').split()])))

file.close()
