from typing import List, Generator, Tuple, Union
from os import path


# Similar to cycle() from itertools
def infinity_iterator(iterable: List[any]) -> Generator[Tuple[int, any], None, None]:
    i: int = 0
    length: int = len(iterable)

    while i < length:
        yield i, iterable[i]

        i = 0 if i == length - 1 else i + 1


def iterate_line_getters(iterable: List[Generator[str, None, None]]) -> str:
    done: List[int] = []

    for idx, i in infinity_iterator(iterable):
        if len(done) == len(iterable):
            break

        if idx in done:
            continue

        try:
            yield next(i)
        except StopIteration:
            done.append(idx)


def get_line(filepath: str) -> Generator[str, None, None]:
    with open(filepath) as file:
        for line in file.readlines():
            yield line


def write_shuffled(out_filepath: str, files: List[str]) -> None:
    iterators: List[Generator[str]] = [get_line(f) for f in files]

    with open(out_filepath, mode='w') as out_file:
        for line in iterate_line_getters(iterators):
            out_file.write(line[0])


def resolve_paths(file_names: Union[List[str], str], dir_name: str) -> List[str]:
    def get_abs_path(filename: str) -> str:
        return path.abspath(path.join(dir_name, filename))

    return list(map(get_abs_path, file_names)) if isinstance(file_names, list) else get_abs_path(file_names)


file_names: List[str] = [
    'I will not betray myself.txt',
    'I don\'t cry, don\'t call, don\'t regret.txt'
]

dir_name: str = 'assets'
file_paths: List[str] = resolve_paths(file_names, dir_name)
out_file_path: str = resolve_paths('result.txt', dir_name)

write_shuffled(out_file_path, file_paths)

# NOTICE
# Create a folder 'assets' and then insert there attached files
# You can try to use any other files in any count, not only two
# If you wanna use your files, please, edit 'filenames' variable
