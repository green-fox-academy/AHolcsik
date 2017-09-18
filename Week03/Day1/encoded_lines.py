# Create a method that decrypts encoded-lines.txt

import string

file_name = "encoded_lines.txt"

def caesar(file_name, shift):
    f = open(file_name, "r")
    shift %= 26
    alphabet_lower = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase

    shifted_alphabet_lower = alphabet_lower[shift:] + alphabet_lower [:shift]
    shifted_alphabet_upper = alphabet_upper[shift:] + alphabet_upper [:shift]

    alphabet = alphabet_lower + alphabet_upper
    shifted_alphabet = shifted_alphabet_lower + shifted_alphabet_upper

    table = string.maketrans(alphabet, shifted_alphabet)

    return plaintext.translate(table)

#def decrypt(file_name):
#    f = open(file_name, "r")
#    decrypted = ""
#    for element in f.read():
#        for char in alphabet:
#            if char == element:
#                decrypted += char(-1)
#    print(decrypted)

#decrypt(file_name)
print(caesar(file_name, 1))