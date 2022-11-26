def larger_sum(list1, list2):
    list1sum = 0
    list2sum = 0

    for item in list1:
        list1sum += item
    for item in list2:
        list2sum += item

    if list1sum >= list2sum:
        return list1
    else:
        return list2
    
print(larger_sum([1, 9, 5], [2, 3, 7]))