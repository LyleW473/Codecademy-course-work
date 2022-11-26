def append_sum(list):
    for i in range(0, 3):
        list.append(list[-1] + list[-2])
    return list

list = [1, 1, 2]
append_sum(list)
print(list)