# - Write a function called `sum` that sum all the numbers
#   until the given parameter

def sum(num):
    total = 1
    for n in range(1, num):
        total *= n+1
    print(total)

sum(3)