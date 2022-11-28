def unique_english_letters(word):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    used_letters = ""
    unique_letter_count = 0
    
    # Iterate through the letters in the word
    for letter in word:
        # If the letter is in the alphabet and not in the used letters 
        if letter in alphabet and letter not in used_letters:
            # Increment unique letter counter 
            unique_letter_count += 1
            # Concatenate the letter onto the used letters string
            used_letters = used_letters + letter

    return unique_letter_count

print(unique_english_letters("mississippi"))
print(unique_english_letters("Apple"))
