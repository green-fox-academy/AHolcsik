# Create a method that decrypts encoded-lines.txt

file_name = "encoded_lines.txt"

def decrypt(file_name):
    f = open(file_name, "r")
    decrypted = ""
    for element in f.readlines()[::-1]:
        decrypted += element
    print(decrypted)

decrypt(file_name)