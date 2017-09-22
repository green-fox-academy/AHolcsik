from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.

def draw_line(x,y):
    canvas.create_line(x, y, x + 150, y + 150, fill = 'black')

def go_to_center(x, y, run):
    if run == 0:
        return
    else:
        draw_line(x,y)
        canvas.create_line(x+10, y, x + 150, y + 150, fill = 'black')
        canvas.create_line(x, y+10, x + 150, y + 150, fill = 'black')
        

go_to_center(0, 0, 100)

root.mainloop()
