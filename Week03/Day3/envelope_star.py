from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/envelope-star/r2.png]

steps = 10

def upper_left_web(steps, x_start, y_start, x_end, y_end):
    for i in range(16):
        canvas.create_line(x_start, y_start, x_end, y_end, fill='purple')
        x_start += steps
        y_end += steps

def upper_right_web(steps, x_start, y_start, x_end, y_end):
    for i in range(16):
        canvas.create_line(x_start, y_start, x_end, y_end, fill='purple')
        x_start += steps
        y_end += steps

def lower_left_web(steps, x_start, y_start, x_end, y_end):
    for i in range(16):
        canvas.create_line(x_start, y_start, x_end, y_end, fill='green')
        y_start += steps
        x_end += steps

def lower_right_web(steps, x_start, y_start, x_end, y_end):
    for i in range(16):
        canvas.create_line(x_start, y_start, x_end, y_end, fill='green')
        y_start += steps
        x_end += steps

upper_left_web(steps, 0, 0, 150, 0)
upper_right_web(steps, 0, 150, 150, 150)
lower_left_web(steps, 0, 150, 150, 150)
lower_right_web(steps, 150, 300, 300, 150)


root.mainloop()
