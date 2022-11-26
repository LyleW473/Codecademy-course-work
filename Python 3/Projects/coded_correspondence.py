message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
decoded_message = ""
alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

# Step 1:
for letter in message:
    if letter in alphabet:
        # print(alphabet.find(letter))
        # print(alphabet.find(letter) + 10)
        # print(alphabet[alphabet.find(letter) + 10])
        decoded_message = decoded_message + alphabet[alphabet.find(letter) + 10]

print(decoded_message)


# Step 2:
my_message = "Yes, I got your message. Send me more messages"
encrypted_message = ""

for letter in my_message.lower():
    if letter in alphabet:
        encrypted_message = encrypted_message + alphabet[alphabet.find(letter) - 10]

print(encrypted_message)

# Decoding my message
decoded_message = ""
for letter in encrypted_message:
    if letter in alphabet:
        # print(alphabet.find(letter))
        # print(alphabet.find(letter) + 10)
        # print(alphabet[alphabet.find(letter) + 10])
        decoded_message = decoded_message + alphabet[alphabet.find(letter) + 10]

print(decoded_message)

# Step 3:

def decoder(message, offset):
    decoded_message = ""

    for letter in message:
        if letter in alphabet:
            # print(letter)
            # print(alphabet[alphabet.find(letter) + offset])
            decoded_message = decoded_message + alphabet[alphabet.find(letter) + offset]

    return decoded_message

print(decoder("jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.", 10))
print(decoder("bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!", 14))


def coder(message, offset):

    encrypted_message = ""
    for letter in message.lower():
        if letter in alphabet:
            encrypted_message = encrypted_message + alphabet[alphabet.find(letter) - offset]
    return encrypted_message


# Step 4:

def step_4_decoder(message):
    for i in range(1,26):
        print("cycle:" + str(i))
        print(decoder(message, i) + "\n")
    
print(step_4_decoder("vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."))

# Step 5:

# Manual version:

# # Convert into new message using keyword
# new_message = "" 
# for i in range(0, len(coded_message)):
#     # Check if the letter is in the alphabet
#     if coded_message[i] in alphabet:
#         # Check if the keyword has no characters in it. If it doesn't, then reset it.
#         if len(keyword) == 0:
#             keyword = "friends"
#         # If it is, add a keyword character to the new message
#         new_message = new_message + keyword[0]
#         # Remove the first letter of the keyword
#         keyword = keyword[1:]   
#     # If it isn't that means it is whitespace, and exclamation mark, etc.
#     else:
#         # Just add the character to the message as it is
#         new_message = new_message + coded_message[i]

# # Cycle through both of the messages and convert them into numbers according to where they are in the alphabet
# character_list = []

# for i in range(0, len(coded_message)):
#     # If the character is a letter (i.e. in the alphabet)
#     if coded_message[i] in alphabet:
#         # Convert the character into an integer (this is so that I can distinguish between letters and things like exclamation marks) and add the character's resulting place value to the character list.
#         character_list.append(int(alphabet.find(coded_message[i]) - alphabet.find(new_message[i])))
#     # If the character is an: exclamation mark, white space, etc.
#     else:
#         # Just add it to the character list as it is
#         character_list.append(coded_message[i])

# # Decode the message
# decoded_message = ""
# for character in character_list:

#     if type(character) == int:
#         decoded_message = decoded_message + alphabet[int(character)]
#     else: 
#         decoded_message = decoded_message + character

# print(decoded_message)

# Function version:

def vigenere_cipher(coded_message, keyword):
    keywords_reset = keyword

    # Convert into new message using keyword
    new_message = "" 
    for i in range(0, len(coded_message)):
        # Check if the letter is in the alphabet
        if coded_message[i] in alphabet:
            # Check if the keyword has no characters in it. If it doesn't, then reset it.
            if len(keyword) == 0:
                keyword = keywords_reset
            # If it is, add a keyword character to the new message
            new_message = new_message + keyword[0]
            # Remove the first letter of the keyword
            keyword = keyword[1:]   
        # If it isn't that means it is whitespace, and exclamation mark, etc.
        else:
            # Just add the character to the message as it is
            new_message = new_message + coded_message[i]

    # Cycle through both of the messages and convert them into numbers according to where they are in the alphabet
    character_list = []

    for i in range(0, len(coded_message)):
        # If the character is a letter (i.e. in the alphabet)
        if coded_message[i] in alphabet:
            # Convert the character into an integer (this is so that I can distinguish between letters and things like exclamation marks) and add the character's resulting place value to the character list.
            character_list.append(int(alphabet.find(coded_message[i]) - alphabet.find(new_message[i])))
        # If the character is an: exclamation mark, white space, etc.
        else:
            # Just add it to the character list as it is
            character_list.append(coded_message[i])

    # Decode the message
    decoded_message = ""
    for character in character_list:
        # Check if the character is an integer, if it is it refers to the place value in the alphabet the letter is at , so we should convert it back into a letter.
        if type(character) == int:
            decoded_message = decoded_message + alphabet[int(character)]
        # If it isn't a character (exclamation mark, whitespace, etc.)
        else: 
            # Just add the character as it is to the decoded message
            decoded_message = decoded_message + character

    return decoded_message

coded_message = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
keyword = "friends"

print(vigenere_cipher(coded_message, keyword))
        
# Step 6:

def coding_vigenere_cipher(original_message, keyword):
    keywords_reset = keyword
    # Convert into new message using keyword
    converted_message = "" 

    for i in range(0, len(original_message)):
        # Check if the letter is in the alphabet. The lower is in case that the message has a capital letter
        if original_message[i].lower() in alphabet:
            # Check if the keyword has no characters in it. If it doesn't, then reset it.
            if len(keyword) == 0:
                keyword = keywords_reset
            # If it is, add a keyword character to the new message
            converted_message = converted_message + keyword[0]
            # Remove the first letter of the keyword
            keyword = keyword[1:]   
        # If it isn't that means it is whitespace, and exclamation mark, etc.
        else:
            # Just add the character to the message as it is
            converted_message = converted_message + original_message[i]

    # Cycle through both of the messages and convert them into numbers according to where they are in the alphabet
    character_list = []

    for i in range(0, len(original_message)):
        # If the character is a letter (i.e. in the alphabet)
        if converted_message[i] in alphabet:
            # Convert the character into an integer (this is so that I can distinguish between letters and things like exclamation marks) and add the character's resulting place value to the character list.
            character_list.append(int(alphabet.find(converted_message[i]) + alphabet.find(original_message[i].lower())))
        # If the character is an: exclamation mark, white space, etc.
        else:
            # Just add it to the character list as it is
            character_list.append(original_message[i])

    # Decode the message
    coded_message = ""
    for character in character_list:
        # Check if the character is an integer, if it is it refers to the place value in the alphabet the letter is at , so we should convert it back into a letter.
        if type(character) == int:
            coded_message = coded_message + alphabet[int(character)]
        # If it isn't a character (exclamation mark, whitespace, etc.)
        else: 
            # Just add the character as it is to the coded message
            coded_message = coded_message + character

    return coded_message

original_message = "Hello, this will be my final message"
test_step_6 = coding_vigenere_cipher(original_message, "hours")
print(test_step_6)

print(vigenere_cipher(test_step_6, "hours"))