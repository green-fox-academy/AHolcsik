from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/line-play/r1.png]

steps = 10

def purple_web(steps):
    x_start = 20
    y_start = 0
    x_end = 300
    y_end = 10
    for i in range(1, 300):
        canvas.create_line(x_start, y_start, x_end, y_end, fill='purple')
        x_start += steps
        y_end += steps

def green_web(steps):
    x_start = 0
    y_start = 20
    x_end = 20
    y_end = 300
    for i in range(1, 300):
        canvas.create_line(x_start, y_start, x_end, y_end, fill='green')
        y_start += steps
        x_end += steps

green_web(steps)
purple_web(steps)
root.mainloop()
