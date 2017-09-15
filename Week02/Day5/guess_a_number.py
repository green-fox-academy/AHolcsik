
add_range_min, add_range_max = map(int, input("Give me the range of numbers (two numbers, split by space): ").split())
lives = int(input("How many tries do you want to have? "))

import random
for x in range(1):
    x = (random.randint(add_range_min, add_range_max))

def compare_numbers(x, lives):
    user_guess = int(input("What is your guess? "))
    while user_guess != x:
        while lives > 0:
            if user_guess < x:
                lives -= 1
                print("Too low! You have", lives , "guesses left")
                if lives == 0:
                    print("I'm sorry! You ran out of guesses")
                    print("The number was" , x)
                    return

                user_guess = int(input("Guess again! "))
            elif user_guess > x:
                lives -= 1
                print("Too high! You have", lives , "guesses left")
                if lives == 0:
                    print("I'm sorry! You ran out of guesses")
                    print("The number was" , x)
                    return

                user_guess = int(input("Guess again! "))
    if user_guess == x:
        print("Congrats! You guessed correctly! The number was", x)
    

compare_numbers(x, lives)
#print (add_range_min, add_range_max)
#print (x)



