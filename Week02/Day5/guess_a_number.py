
add_range_min, add_range_max = map(int, input("Give me the range of numbers (two numbers, split by space): ").split())

import random
for x in range(1):
    x = (random.randint(add_range_min, add_range_max))

def compare_numbers(x):
    user_guess = int(input("What is your guess? "))
#    while user_guess != x:
    if user_guess < x:
        print("Too low! Guess again!")
    elif user_guess > x:
        print("Too high! Guess again!")
    else:
        print("Congrats! You guessed correctly! The number was ", x)
    

compare_numbers(x)
print (add_range_min, add_range_max)
print (x)



