from tkinter import *

root = Tk()

canvas = Canvas(root)
canvas.pack()
canvas_width = 300
canvas_height = 300

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps/r3.png]


nsteps = 5

def bigger_boxes(nsteps):
    size = 10
    x = 0
    y = 0
    for i in range(nsteps):
        x_e = x + size
        y_e = y + size
        purple_square = canvas.create_rectangle(x, y, x_e, y_e, fill='purple')
        size += 10
        x = x_e
        y = y_e

bigger_boxes(nsteps)
root.mainloop()
