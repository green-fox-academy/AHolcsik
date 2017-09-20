from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.

square_1 = 20
square_2 = 50
square_3 = 100

def center_square(x):
    square = canvas.create_rectangle (150 - (x/2), 150 - (x/2), 150 + (x/2), 150 + (x/2))

center_square(square_1)
center_square(square_2)
center_square(square_3)

root.mainloop()
