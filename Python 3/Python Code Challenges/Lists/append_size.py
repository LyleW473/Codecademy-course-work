def append_size(list):
    list.append(len(list))

    return list

list = [23, 42, 108]
append_size(list)
print(list)