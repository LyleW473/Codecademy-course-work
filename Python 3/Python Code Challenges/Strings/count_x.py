def count_char_x(word, x):
    x_count = 0

    for letter in word:
        if letter == x:
            x_count += 1

    return x_count

print(count_char_x("mississippi", "s"))
print(count_char_x("mississippi", "m"))