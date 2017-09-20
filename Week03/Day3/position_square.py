from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.

x1 = 43
y1 = 170

x2 = 90
y2 = 200

x3 = 189
y3 = 46

def square(x, y):
    new_square = canvas.create_rectangle(x, y, (x + 50), (y + 50))

square(x1,y1)
square(x2,y2)
square(x3,y3)

root.mainloop()





root.mainloop()
