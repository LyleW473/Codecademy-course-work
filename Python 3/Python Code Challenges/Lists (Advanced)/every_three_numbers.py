def every_three_nums(start):
    list = []
    if start > 100:
        pass
    else:
        for i in range(start, 101, 3):
            list.append(i)

    return list
    
print(every_three_nums(101))