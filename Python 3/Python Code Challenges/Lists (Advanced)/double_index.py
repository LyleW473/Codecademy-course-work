def double_index(list, index):
    if 0 < index < len(list) - 1:
        new_list = list.copy()
        new_list[index] *= 2
        return new_list
    else:
        return list

print(double_index([3, 8, -10, 12], 2))