from tkinter import *

root = Tk()

canvas = Canvas(root, width='500', height='500', bg='yellow')
canvas.pack()

def squares(size, x, y):
    if size < 5:
        return 0
    else: 
        line1 = canvas.create_line(x + size/3, y, x + size/3, y + size, fill='black')
        line2 = canvas.create_line(x + size/3*2, y, x + size/3*2, y + size, fill='black')
        line3 = canvas.create_line(x, y + size/3, x + size, y + size/3, fill='black')
        line4 = canvas.create_line(x, y + size/3*2, x + size, y + size/3*2, fill='black')
        return squares((size/3), x + size/3, y), squares((size/3), x, y + size/3), squares((size/3), x + size/3*2, y + size/3), squares((size/3), x + size/3, y + size/3*2)

print(squares(500, 0, 0))

root.mainloop()
