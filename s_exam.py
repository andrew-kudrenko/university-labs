def some(a, b):
    for i in range(len(a)):
        if a[i] in b:
            return True

    return False


def handle(a, b):
    has_same = some(a, b)

    if not has_same:
        print('The array has not items in common')
        return

    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j + 1], a[j] = a[j], a[j + 1]

    file = open('task_output.txt', mode='w', encoding='utf-8')
    file.write(str(a))
    file.close()


a = [int(n) for n in input('Enter the first: ').split()]
b = [int(n) for n in input('Enter the second: ').split()]

handle(a, b)