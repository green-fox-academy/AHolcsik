from tkinter import *

root = Tk()

canvas = Canvas(root, width='500', height='500')
canvas.pack()

def squares(size):
    x = 0
    y = 0
    if size > 10:
        return 0
    else: 
        canvas.create_line(x + size/3, y, x + size/3, y + size)
        canvas.create_line(x + size/3*2, y, x + size/3*2, y + size)
        canvas.create_line(x, x + size/3, x + size, y + size/3)
        canvas.create_line(x, x + size/3*2, x + size, y + size/3*2)
        return (  )

print(squares(size))

root.mainloop()
