def add_ten(my_dictionary):
    for key in my_dictionary.keys():
        my_dictionary[key] = my_dictionary[key] + 10
    return my_dictionary

print(add_ten({1:5, 2:2, 3:3}))