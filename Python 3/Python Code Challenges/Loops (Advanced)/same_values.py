def same_values(list1, list2):
    index_list = []
    for i in range(0, len(list1)):
        if list1[i] == list2[i]:
            index_list.append(i)
    return index_list 

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))