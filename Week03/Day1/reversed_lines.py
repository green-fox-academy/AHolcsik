# Create a method that decrypts reversed-lines.txt

file_name = "reversed_lines.txt"

def decrypt(file_name):
    f = open(file_name, "r")
    decrypted = ""
    for element in f.read()[::-1]:
        decrypted += element
    print(decrypted)

decrypt(file_name)