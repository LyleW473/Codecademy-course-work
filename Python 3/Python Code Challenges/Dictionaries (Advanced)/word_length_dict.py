def word_length_dictionary(words):
    new_dictionary = {}
    for word in words:
        new_dictionary[word] = len(word)
    return new_dictionary

print(word_length_dictionary(["apple", "dog", "cat"]))
print(word_length_dictionary(["a", ""]))