def odd_indices(list):
    new_list = []
    for i in range(0, len(list)):
        if i % 2 != 0:
            new_list.append(list[i])
    return new_list

print(odd_indices([4, 3, 7, 10, 11, -2]))