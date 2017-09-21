# We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies recursively (without loops or multiplication).

def ears_o_bunnies(num):
    if num == 1:
        return 2
    else:
        return 2 + (ears_o_bunnies(num-1))
    
print(ears_o_bunnies(6))
