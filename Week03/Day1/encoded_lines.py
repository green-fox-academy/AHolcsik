# Create a method that decrypts encoded-lines.txt

file_name = "encoded_lines.txt"
shift = 1

def decrypt(file_name, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    f = open(file_name, "r")
    decrypted = ""
    for element in f.read():
        decrypted += element
    print(decrypted)

decrypt(file_name, shift)