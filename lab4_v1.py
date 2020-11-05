def merge_list(a, b):
    merged = a + b

    for i in range(len(merged)):
        for w in range(len(merged) - 1):
            if merged[w] < merged[w + 1]:
                e = merged[w]
                merged[w] = merged[w + 1]
                merged[w + 1] = e

    return merged


a = [21, 45, 65, 43, 31, 567, 89, 10]
b = [-21, -45, 90000000, -43, -31, -567, -89, -10]

print(merge_list(a, b))
