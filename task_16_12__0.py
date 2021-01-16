def inverted(line) -> str:
    result: str = ''
    word_starts: int = 0

    for i in range(len(line)):
        if (i == len(line) - 1) or ((i > 0) and (line[i - 1] != ' ') and (line[i] == ' ')):
            word_ends = i if i == len(line) - 1 else i - 1

            for j in range(word_ends, word_starts - 1, -1):
                result += line[j]

        elif ((i == 0) or (line[i - 1] == ' ')) and (line[i] != ' '):
            word_starts = i - 1
        elif line[i] == ' ':
            result += line[i]

    return result


data = '   ABC DEFG HIJK      LMNOP'

print(f'It was: {data}\nNow is: {inverted(data)}')
