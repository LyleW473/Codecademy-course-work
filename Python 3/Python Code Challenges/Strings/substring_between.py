def substring_between_letters(word, start, end):
    # If the index at which the starting letter and the ending letter, both are not -1.
    if word.find(start) != -1 and word.find(end) != -1:
        # Slice the word from the letter after the starting letter to the letter before the ending letter.
        new_word = word[word.find(start) + 1: word.find(end)]
    # Otherwise, return the original string (because the letter is not in the string)
    else:
        new_word = word
    return new_word

print(substring_between_letters("apple", "p", "e"))
print(substring_between_letters("apple", "p", "c"))