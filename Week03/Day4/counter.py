# Write a recursive function that takes one parameter: n and counts down from n.

num = 10

def counter(num):
    print(num)
    if num == 0:
        return(num)
    else:
        return(counter(num-1))

counter(num)