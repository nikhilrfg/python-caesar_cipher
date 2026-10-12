# Caesar cipher.
text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)
    




# Lab 2.5.1 - The Caesar Cipher: Encrypting a Message
#
# Assumptions:
# 1. The program accepts Latin letters only.
# 2. All letters of the message are converted to uppercase.
# 3. Non-alphabetic characters are ignored.
# 4. Each letter is replaced by the next letter in the alphabet.
# 5. The letter Z wraps around and becomes A.
#
# Tracing:
# Line 02: Ask the user to enter the open (unencrypted) message.
# Line 03: Prepare an empty string for the encrypted message.
# Line 04: Iterate through every character in the message.
# Line 05: Check if the current character is not alphabetic.
# Line 06: Ignore non-alphabetic characters using continue.
# Line 07: Convert the current letter to uppercase.
# Line 08: Get the character code using ord() and increase it by 1.
# Line 09: Check whether the new code has gone past Z.
# Line 10: If it has, change the code to the code for A.
# Line 11: Convert the code back to a character using chr()
#          and append it to the encrypted message.
# Line 13: Print the encrypted message.