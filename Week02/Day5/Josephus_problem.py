
import math

number_of_people = int(input("Hey, Josephus! What's the number of peeps? "))

def highest_power_of_two(number_of_people):
    return 2 ** int(math.log(number_of_people, 2))

rest = number_of_people - highest_power_of_two(number_of_people)

def winner_is(rest):
    print("Sit on the seat with number '", 2 * rest + 1, "' on it. You're welcome!")

winner_is(rest)

