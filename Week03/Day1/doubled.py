# Create a method that decrypts the duplicated-chars.txt

file_name = "duplicated_chars.txt"

def decrypt(file_name):
    f = open (file_name, "r")
    decrypted = ()
    for element in f.read():
        if element != decrypted[-1]:
            decrypted += element
    print(decrypted)

decrypt(file_name)

