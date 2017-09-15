import math

num = 2
base = 4

def floor_log(num, base):

    if num == 0:
        return 0

    return base ** int(math.log(num, base))

floor_log(num, base)
print(num, base)