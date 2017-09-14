# Write a program that asks for two integers
# The first represents the number of chickens the farmer has
# The seconf represents the number of pigs the farmer has
# It should print how many legs all the animals have

chickens = input("How many chickens does the farmer have? ")
pigs = input("how many pigs does the farmer have? ")

def legs(chickens, pigs):
    number_of_legs = 0
    number_of_legs += int(chickens) * 2
    number_of_legs += int(pigs) * 4
    print("The lifestock has" , number_of_legs , "legs!")

legs(chickens, pigs)


