def balance(a, b):
    if len(a) > len(b):
        for i in range(len(b), len(a)):
            b += a[i]
    else:
        for i in range(len(a), len(b)):
            a += b[i]

    return a, b


a = input('First string: ')
b = input('Second string: ')

a, b = balance(a, b)

print(f'First: {a}\nSecond: {b}')
