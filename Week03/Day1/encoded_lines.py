# Create a method that decrypts encoded-lines.txt

import string

file_name = "Uif [fo pg Qzuipo"

alphabet = string.ascii_lowercase + string.ascii_uppercase


# def decrypt(file_name, start = -1):
#     f = open(file_name, "r")
#     n = start
#     decrypted = ""
#     for element in f.read():
#         for char in alphabet:
#             if char == element:
#                 decrypted += char(-1)
#     print(decrypted)

# decrypt(file_name)


def decode(file_name):
    global alpha
    global alphaupper
    words = cleartext.replace(cleartext[len(cleartext) - 1], "")
    words = words.replace(words[0], "")
    cyphertext = ""
    for char in words:
        if char in alphaupper:
            newpos = (alphaupper.find(char) + 27) % 26
            cyphertext += alphaupper[newpos]
        elif char in alpha:
            newpos = (alpha.find(char) + 27) % 26
            cyphertext += alpha[newpos]
        else:
            cyphertext += char
    return cyphertext

print(decode)