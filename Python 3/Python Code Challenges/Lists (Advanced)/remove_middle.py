def remove_middle(list, start, end):
    return list[0:start] + list[end + 1:len(list)]

print(remove_middle([4, 8 , 15, 16, 23, 42], 1, 3))