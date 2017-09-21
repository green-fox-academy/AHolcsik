from tkinter import *

root = Tk()

canvas = Canvas(root, width='500', height='500')
canvas.pack()

size = 300

def squares(size):
    if size < 10:
        return
    else: 
        canvas.create_rectangle(100, 100, 100 + size, 100 + size)

print(squares(size))

root.mainloop()
