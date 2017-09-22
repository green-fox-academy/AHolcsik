from tkinter import *
import math

root = Tk()

canvas = Canvas(root, width='500', height='500')
canvas.pack()


def draw_circle(x, y, size):
    canvas.create_oval(x, y, x + size, y + size,
                          fill = '', outline = 'black')
        
def draw_fractal(x, y, size):
    if size < 50:
        return
    else:
        m = (size / 2) * 1.5
        side = math.sqrt(m ** 2)
        circle_position_x = math.sqrt(math.sqrt(side ** 2) - math.sqrt((size / 3) **2))
        height = math.sqrt(3) / 2 * size
        draw_circle(x, y, size)
        draw_fractal(x + size / 4, y, size / 2)
        draw_fractal(x + circle_position_x, y + side / 2, size / 2)
        draw_fractal(x + circle_position_x * 16, y + side / 2, size / 2)
        

draw_fractal(0, 0, 500) 

root.mainloop() 