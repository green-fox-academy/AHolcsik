from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# divide the canvas into 4 equal parts
# and repeat this pattern in each quarter:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/line-play/r1.png]

steps = 10

def purple_web(steps, x_start, y_start, x_end, y_end):
    for i in range(16):
        canvas.create_line(x_start, y_start, x_end, y_end, fill='purple')
        x_start += steps
        y_end += steps

def green_web(steps, x_start, y_start, x_end, y_end):
    for i in range(16):
        canvas.create_line(x_start, y_start, x_end, y_end, fill='green')
        y_start += steps
        x_end += steps

purple_web(steps, 0, 0, 150, 0)
purple_web(steps, 150, 0, 300, 0)
purple_web(steps, 0, 150, 150, 150)
purple_web(steps, 150, 150, 300, 150)

green_web(steps, 0, 0, 0, 150)
green_web(steps, 150, 0, 150, 150)
green_web(steps, 0, 150, 0, 300)
green_web(steps, 150, 150, 150, 300)

root.mainloop()
