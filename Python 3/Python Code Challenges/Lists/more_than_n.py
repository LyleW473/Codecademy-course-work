def more_than_n(list, item, n):
    if list.count(item) > n:
        return True
    return False

list = [3,2,5,6,7,1,2,3,3,3,3,3]
print(more_than_n(list, 3, 4))