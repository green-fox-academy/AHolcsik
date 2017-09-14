# Write a program that asks for 5 integers in a row,
# then it should print the sum and the average of these numbers like:
#
# Sum: 22, Average: 4.4

numbers = input("Give me a number: "), input("Another: "), input("And another: "), input("... And another: "), input("And one more: ")

def calculator(numbers):
    summa = 0
    for element in numbers:
        summa += int(element)
    print("Sum: ", summa)
    average = summa / 5
    print("Average: " , average)
    
    

calculator(numbers)
