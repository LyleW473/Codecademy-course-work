def middle_element(list):
    if len(list) % 2 != 0:
        return list[len(list) // 2]
    else:
        return (list[(len(list) // 2)- 1] + list[(len(list) // 2)]) / 2

#print(middle_element([5, 2, -10, -4, 4, 5]))
print(middle_element([5, 2, -4, 4, 5]))