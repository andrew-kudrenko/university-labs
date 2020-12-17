def balance(a, b):
    if a > b:
        for i in range(len(b), len(a)):
            b += a[i]
    else:
        for i in range(len(a), len(b)):
            a += b[i]

    return a, b


a = 'ABCDEF'
b = 'GHIJKLMNOPQR'

a, b = balance(a, b)

print(f'First: {a}\nSecond: {b}')
