def remove_col(matrix, target):
    handled = []

    for row in range(len(matrix)):
        current = []

        for col in range(len(matrix[row])):
            if col != target:
                current.append(col)

        handled.append(current)

    return handled

example = [
    [0, 1, 2, 3],
    [0, 1, 2, 3],
    [0, 1, 2, 3],
    [0, 1, 2, 3],
]

print(remove_col(example, 1))
