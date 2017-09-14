# Write a program that reads a number from the standard input, then draws a
# triangle like this:
#
# *
# **
# ***
# ****
#
# The triangle should have as many lines as the number was

lines = int(input("How many lines should I draw? "))

def draw_triangle(lines):
    a = 1
    while a <= lines:
        print("*" * a)
        a += 1

draw_triangle(lines)