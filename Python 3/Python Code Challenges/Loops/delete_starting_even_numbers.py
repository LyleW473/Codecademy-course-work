def delete_starting_evens(list):

    while len(list) > 0 and list[0] % 2 == 0:
        list = list[1:]
        
    return list

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))