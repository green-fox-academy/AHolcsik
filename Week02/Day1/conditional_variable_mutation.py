a = 24
out = 0
# if w is even increment out by one

def is_it_even(a):
    out = 0
    if a % 2 == 0:
        out += 1
    print(out)

is_it_even(a)


b = 13

# if b is between 10 and 20 set out2 to "Sweet!"
# if less than 10 set out2 to "More!",
# if more than 20 set out2 to "Less!"

def between_range(b):
    out2 = ""
    if 10 < b < 20:
        out2 = "Sweet!"
    elif b < 10:
        out2 = "More!"
    else:
        out2 = "Less!"
    print(out2)

between_range(b)


c = 123
credits = 100
is_bonus = False
# if credits are at least 50,
# and is_bonus is false decrement c by 2
# if credits are smaller than 50,
# and is_bonus is false decrement c by 1
# if is_bonus is true c should remain the same

def vary_c(c):
    if credits >= 50 and is_bonus == False:
        c -= 2
    elif credits < 50 and is_bonus == False:
        c -= 1
    elif is_bonus == True:
        c = c
    print(c)

vary_c(c)


d = 8
time = 120
out3 = ""
# if d is dividable by 4
# and time is not more than 200
# set out3 to "check"
# if time is more than 200
# set out3 to "Time out"
# otherwise set out3 to "Run Forest Run!"

def whats_the_time(value, time):
    if value % 4 == 0 and time <= 200:
        out3 = "check"
    elif time > 200:
        out3 = "Time out"
    else:
        out3 = "Run Forest Run!"
    print(out3)

whats_the_time(d, time)
