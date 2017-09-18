# Create a method that decrypts reversed-order.txt

file_name = "reversed_order.txt"


def decrypt(file_name):
    f = open(file_name, "r")
    decrypted = ""
    for element in f.readlines()[::-1]:
        decrypted += element
    print(decrypted)

decrypt(file_name)

    
    