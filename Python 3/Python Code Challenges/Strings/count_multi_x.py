def count_multi_char_x(word, x):
    # Returns an array with the characters before and after where x was found
    split_word = word.split(x)

    return (len(split_word) - 1) # The length should be one less because the length of split word represents how many split sections there are 

print(count_multi_char_x("mississippi", "iss"))
print(count_multi_char_x("apple", "pp"))