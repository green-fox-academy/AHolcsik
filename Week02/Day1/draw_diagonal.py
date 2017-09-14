# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%
# %%  %
# % % %
# %  %%
# %   %
# %%%%%
#
# The square should have as many lines as the number was

lines = int(input("How many lines should I draw? "))

#def draw_triangle(lines):
#    a = lines
#    for i in (lines):
#        for j in i:
#            print("%" * int(a))

#draw_triangle(lines)

def create_grid(lines):
    grid = []
    for i in range(lines):
        row_list = []
        for j in range(lines):
            if j == i:
                row_list.append("1")
            else:    
                row_list.append ("0")
        grid.append (row_list)
    return grid

def print_grid(grid):
    for row in int(grid):
        print(row)

print_grid(lines)


