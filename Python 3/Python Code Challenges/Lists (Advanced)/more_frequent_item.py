def more_frequent_item(list, item1, item2):
    if list.count(item1) >= list.count(item2):
        return item1
    else:
        return item2

print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))