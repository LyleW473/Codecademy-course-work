def frequency_dictionary(words):
    new_dictionary = {}
    for word in words:
        if word not in new_dictionary.keys():
            new_dictionary[word] = 0
        if word in new_dictionary.keys():
            new_dictionary[word] += 1
    return new_dictionary
print(frequency_dictionary(["apple", "apple", "cat", 1]))
print(frequency_dictionary([0,0,0,0,0]))