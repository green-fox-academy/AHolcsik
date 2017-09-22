from tkinter import *
import math
root = Tk()

canvas = Canvas(root, width='500', height='500')
canvas.pack()


def koch (x, y, size):
    side = size / 3
    height = math.sqrt(side ** 2 - side ** 2)
    canvas.create_polygon(x, y + height, 
                          x + side, y + height,
                          x + side * 1.5, y,
                          x + 2 * side, y + height
                          x + size, y + height,
                          x + (size - side / 2), y 
                          
                          )

        

# def draw_fractal(x, y, size):
#     if size < 10:
#         return
#     else:

koch(0, 0, 300)

root.mainloop()