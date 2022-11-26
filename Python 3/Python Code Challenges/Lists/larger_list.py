def larger_list(list1, list2):
    if len(list1) > len(list2) or len(list1) == len(list2):
        return list1[-1]
    elif len(list2) > len(list1):
        return list2[-1]