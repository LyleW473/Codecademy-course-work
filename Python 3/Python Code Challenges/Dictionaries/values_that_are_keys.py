def values_that_are_keys(my_dictionary):
    parents_of_children = []

    for value in my_dictionary.values():
        if value in my_dictionary.keys():
            parents_of_children.append(value)
    return parents_of_children

print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))