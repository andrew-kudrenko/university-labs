def dict_from_sequence(sequence):
    digits = {key: False for key in range(10)}

    for number in sequence:
        for digit in str(number):
            if int(digit) in digits:
                digits[int(digits)] = True

    return digits


def extract_unique(digits):
    unique = []

    for key in digits:
        if digits[key]:
            unique.append(digits[key])

    return unique


sequence = [value for value in input('Enter a sequence: ').split()]
print(extract_unique(dict_from_sequence(sequence)))
