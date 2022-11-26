def reversed_list(list1, list2):
    if list1 == list2[::-1]:
        return True
    return False

print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))