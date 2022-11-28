def make_spoonerism(word1, word2):
    # # Create variables with the first letter of each word
    # word1_first_letter = word1[0]
    # word2_first_letter = word2[0]
    # # Set the word to be all of the letters except the first letter
    # word1 = word1[1:]
    # word2 = word2[1:]   
    
    # # Switch the letters around
    # word1 = word2_first_letter + word1
    # word2 = word1_first_letter + word2

    # # Combine them with a space
    # result = word1 + " " +  word2

    # Second method does the same thing as the first
    return word2[0] + word1[1:] + " " + word1[0] + word2[1:]

print(make_spoonerism("Codecademy", "Learn"))
print(make_spoonerism("Hello", "world!"))
print(make_spoonerism("a", "b"))