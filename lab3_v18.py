array = list(map(int, input('Enter an array: ').split()))
sub_array = list(map(int, input('Enter an sub array: ').split()))

intersected = False
is_subset = False

for idx, item in enumerate(array):
    if not sub_array:
        is_subset = True
        break

    if sub_array[0] == item:
        sliced = array[idx:idx+len(sub_array)]

        for s_idx, s_item in enumerate(sliced):
            if s_item != sub_array[s_idx]:
                break

        is_subset = True

        break

print(f'{"Является" if is_subset else "Не является"} подмассивом')
