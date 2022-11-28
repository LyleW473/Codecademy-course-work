def add_exclamation(word):
    while len(word) < 20:
        word = word + "!"
    return word

print(add_exclamation("Codecademy"))
print(add_exclamation("Codecademy is the best place to learn"))
