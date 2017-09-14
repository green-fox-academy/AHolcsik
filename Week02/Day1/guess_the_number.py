# Write a program that stores a number, and the user has to figure it out.
# The user can input guesses, after each guess the program would tell one
# of the following:
#
# The stored number is higher
# The stried number is lower
# You found the number: 8


stored_number = 8
guess = int(input("what is your guess? "))

def guess_the_number(stored_number):
    if guess < stored_number:
        print("The stored number is higher")
    elif guess > stored_number:
        print("The stored numer is lower")
    elif guess == stored_number:
        print("You found the number!")

guess_the_number(stored_number)