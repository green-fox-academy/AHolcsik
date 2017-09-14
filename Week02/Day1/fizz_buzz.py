# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print “Fizz” instead of the number
# and for the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz”.

numbers = list(range(1,101))

def trickiness(numbers):
    for i in numbers:
        if i % 3 == 0 and i % 5 == 0:
            i = "FizzBuzz"
            print(i)
        elif i % 3 == 0:
            i = "Fizz"
            print(i)
        elif i % 5 == 0:
            i = "Buzz"
            print(i)    
        else:
            print(i)

trickiness(numbers)

