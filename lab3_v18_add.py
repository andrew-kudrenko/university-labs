array = [int(n) for n in input('Enter as array: ').split()]
sub_array = [int(n) for n in input('Enter a subarray: ').split()]

is_subset = True

for idx, item in enumerate(array):
    if not sub_array:
        is_subset = False
        break

    if sub_array[0] == item:
        sliced = array[idx:idx+len(sub_array)]

        for s_idx, s_item in enumerate(sliced):
            if s_item != sub_array[s_idx]:
                is_subset = False
                break

        break

print(f'{"Является" if is_subset else "Не является"} подмассивом')