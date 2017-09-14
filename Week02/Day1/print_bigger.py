# Write a program that asks for two numbers and prints the bigger one

a = input("Give me a number: ")
b = input("Give me another number: ")

def bigger(a,b):
    if a < b:
        print(b)
    else:
        print(a)

bigger(a,b)
    