# Write a program that asks for a number.
# It would ask this many times to enter an integer,
# if all the integers are entered, it should print the sum and average of these
# integers like:
#
# Sum: 22, Average: 4.4

numbers = [int(input("Give me a number: ")), int(input("And another: "))]

def new_number(numbers):
    answer = input("Do you want to add another number? y/n ")
#    while answer != "n":
    if answer == "y":
        numbers += int((input("Add another number:"))
    if answer == "n":
        print("Too bad...")
    return(numbers)

#def calculator(numbers):
#    summa = 0
#    for element in numbers:
#        summa += int(element)
#    print("Sum: ", summa)
#    average = summa / len(numbers)
#    print("Average: " , average)

new_number(numbers)
#calculator(numbers)

