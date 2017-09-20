from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

square_1 = 20
square_1_color = 'green'

square_2 = 50
square_2_color = 'purple'

square_3 = 100
square_3_color = 'blue'

def center_square(x,y):
    square = canvas.create_rectangle (150 - (x/2), 150 - (x/2), 150 + (x/2), 150 + (x/2), fill=y)

center_square(square_3, square_3_color)
center_square(square_2, square_2_color)
center_square(square_1, square_1_color)

root.mainloop()
