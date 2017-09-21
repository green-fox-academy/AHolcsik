from tkinter import *

root = Tk()

canvas = Canvas(root, width='500', height='500')
canvas.pack()


def koch (order, size):
    if order == 0:
        canvas.create_line(100, 100, 100+size, 100)
    else:
        koch(order-1, size/3)
        
        
print(koch(0, 300))

root.mainloop()