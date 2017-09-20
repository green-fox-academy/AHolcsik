from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.

x1 = 43
y1 = 170

x2 = 90
y2 = 300

x3 = 289
y3 = 46

def lines_to_center(x, y):
    new_line = canvas.create_line(x, y, 150, 150)

lines_to_center(x1,y1)
lines_to_center(x2,y2)
lines_to_center(x3,y3)
root.mainloop()
