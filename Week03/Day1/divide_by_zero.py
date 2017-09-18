# create a function that takes a number,
# divides ten with it,
# and prints the result.
# it should print "fail" if the parameter is 0

divisor = int(input("Give me a number: "))

try:
    result = 10 / divisor
    print(result)
except ZeroDivisionError:
    print("Can't divide by zero!")

