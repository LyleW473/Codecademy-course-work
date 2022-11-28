def max_key(my_dictionary):
    key_value_list = list(zip(my_dictionary.keys(), my_dictionary.values()))
    greatest_key = 0
    greatest_value = 0

    for key, value in key_value_list:
        if value > greatest_value:
            greatest_value = value
            greatest_key = key
    return greatest_key

print(max_key({1:100, 2:1, 3:4, 4:10}))
print(max_key({"a":100, "b":10, "c":1000}))