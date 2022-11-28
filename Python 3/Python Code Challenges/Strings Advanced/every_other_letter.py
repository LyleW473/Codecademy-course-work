def every_other_letter(word):
    new_string = ""
    for i in range(0, len(word), 2):
        # Concatenate the letter at index i to the new string
        new_string = new_string + word[i]
    return new_string

print(every_other_letter("Codecademy"))
print(every_other_letter("Hello world!"))
print(every_other_letter(""))