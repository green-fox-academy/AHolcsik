import math
number_of_people = int(input("Hey, Josephus! What's the number of peeps? "))

#def solution(number_of_people):
#    remaining = number_of_people
#    while number_of_people != 1:
#        for i in (number_of_people):
#            remaining -= 1

#feed this number_of_people
def highest_power_of_two(number_of_people):
    if number_of_people < 0:
       raise ValueError("Non-negative number only.")

    if number_of_people == 0:
       return 0

    return 2 ** int(math.log(number_of_people, 2))

rest = number_of_people - highest_power_of_two(number_of_people)
#power = number_of_people - rest

def winner_is(rest):
    print("Sit on the seat with number", 2 * rest + 1, "on it. You're welcome!")
    

#the power needs to be determined for formula
#def find_the_power(highest_power_of_two):
#    return int(math.log(a, 2))

#print(find_the_power)
print(winner_is(rest))



#def largestPowerOfTwoThatIsAFactorOf(number_of_people):
#    if number_of_people % 2 != 0: return 1
#    factor = 0
#    while number_of_people % 2 == 0:
#        number_of_people /= 2
#        factor += 1
#    return 2 ** factor

#print(largestPowerOfTwoThatIsAFactorOf(number_of_people))

#def solution_again(number_of_people):
#    while number_of_people != 1:
#        if number_of_people is square root of two 
#            the result is one!
#        if number_of_people is not suare root of two
#            find highest number of power to 2 and decrease it
#            repeat for the rest until a remaining number is left 
#            #does this make sense?
#        the first power of two needs to be excluded
#        the number which "starts" then is the winner!

#if n = 2 ** a + l and l < 2*number
#winner is 2*l + 1

#a is the power of 2 in the given number
#find biggest power of a




    



#def solution_final(a):
#    while number_of_people 

#finding_square_root(number_of_people)
#print(number_of_people)






#in binary it's even easier but that's cheating














#("Sit on the seat with number", number, "on it. You're welcome!")