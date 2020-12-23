def dict_from_sequence(sequence):
    digits = {key: 0 for key in range(10)}

    for number in sequence:
        value = str(number)

        for digit in str(number):
            if (value >= '0') and (value <= '9'):
                key = int(digit)

                if key in digits:
                    digits[key] += 1
    print(digits)
    return digits


def freq_than(digits, count=2):
    extracted = []

    for key in digits:
        if digits[key] > count:
            extracted.append(key)

    return extracted


sequence = [int(value) for value in input('Enter a sequence: ').split()]
print(freq_than(dict_from_sequence(sequence)))
