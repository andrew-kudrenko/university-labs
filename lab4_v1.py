def merge_list(a, b):
    merged = []

    i = j = 0

    while i < len(a) or j < len(b):
        if i == len(a):
            merged += b
            break
        elif j == len(b):
            merged += a
            break

        if a[i] > b[j]:
            merged.append(a[i])
            i += 1

        elif b[j] > a[i]:
            merged.append(b[j])
            j += 1

    return merged


a = [10, 8, 6, 4]
b = [-2, -4, -6, -8, -10]

print(merge_list(a, b))