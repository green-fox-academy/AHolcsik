from tkinter import *
import time

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()


# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.

def draw_line(x, y):
    time.sleep(0.1)
    canvas.update()
    canvas.create_line(x, y, 150, 150, fill = 'black')

def go_to_center_x(x, y):
    if x == 300:
        return
    else:
        draw_line(x,y)
        go_to_center_x(x + 10, y)
        

def go_to_center_y(x, y):
    if y == 0:
        return
    else:
        draw_line(x,y)
        go_to_center_y(x, y - 10)


def come_back_x(x, y, run):
    if run == 0:
        return
    else:
        draw_line(x,y)
        come_back_x(x - 10, y, run -1)

def come_back_y(x, y):
    if y == 300:
        return
    else:
        draw_line(x,y)
        come_back_y(x, y + 10)

go_to_center_x(0, 0)
come_back_y(300, 0)
come_back_x(300, 300, 30)
go_to_center_y(0, 300)

root.mainloop()
