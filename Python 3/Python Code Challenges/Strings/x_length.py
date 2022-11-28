def x_length_words(sentence, x):
    sentence_array = sentence.split(" ")
    # Assume that every single word in the sentence has a length greater than or equal to x
    deciding_boolean = True

    # Iterate through the sentence array
    for word in sentence_array: 
        # If any of the words are less than x, then the deciding boolean becomes False
        if len(word) < x:
            deciding_boolean = False

    return deciding_boolean

print(x_length_words("i like apples", 2))
print(x_length_words("he likes apples", 2))