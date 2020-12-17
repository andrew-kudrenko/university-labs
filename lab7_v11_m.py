from typing import List


def all_done(iterable: List):
    for item in iterable:
        if not item:
            return False

    return True


def read_files(filenames: str) -> List[List[str]]:
    read: List[List[str]] = []

    for filename in filenames:
        file = open(filename, 'r', encoding='utf-8')
        read.append(file.readlines())
        file.close()

    return read


def write_result(filename: str, collections: List[List[str]]):
    file = open(filename, 'w', encoding='utf-8')
    conditions = [False for _ in collections]
    pointers = [0 for _ in collections]

    while not all_done(conditions):
        for idx, lines in enumerate(collections):
            if not conditions[idx]:
                if pointers[idx] >= len(lines):
                    conditions[idx] = True
                else:
                    file.write(lines[pointers[idx]][0])
                    pointers[idx] += 1

    file.close()


filenames = {
    'input': ['lab7_v11_input_0.txt', 'lab7_v11_input_1.txt'],
    'output': 'lab7_v11_output.txt'
}

write_result(filenames['output'], read_files(filenames['input']))
