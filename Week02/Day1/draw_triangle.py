# Write a program that reads a number from the standard input, then draws a
# triangle like this:
#
# *
# **
# ***
# ****
#
# The triangle should have as many lines as the number was

lines = input("How many lines should I draw? ")

def draw_triangle(lines):
    a = []
    for i in lines:
        a += "*"
        print(a)

draw_triangle(lines)