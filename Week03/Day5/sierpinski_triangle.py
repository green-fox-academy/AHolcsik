from tkinter import *
import math

root = Tk()

canvas = Canvas(root, width='500', height='500')
canvas.pack()


def draw_triangle (x, y, size):
    height = math.sqrt(3) / 2 * size
    canvas.create_polygon(x, y, x + size, y, x + size / 2, y + height,
                          fill = '', outline = 'black')
        
def draw_fractal(x, y, size):
    if size < 5:
        return
    else:
        height = math.sqrt(3) / 2 * size
        draw_triangle(x, y, size)
        draw_fractal(x, y, size / 2)
        draw_fractal(x + size / 2, y, size / 2)
        draw_fractal(x + size / 4, y + height / 2, size / 2)

draw_fractal(0, 20, 500) 

root.mainloop() 