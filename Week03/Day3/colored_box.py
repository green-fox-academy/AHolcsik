from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw a box that has different colored lines on each edge.

green_line = canvas.create_line(30, 30, 130, 30, fill = 'green')
blue_line = canvas.create_line(130, 30, 130, 130, fill = 'blue')
purple_line = canvas.create_line(130, 130, 30, 130, fill = 'purple')
orange_line = canvas.create_line(30, 130, 30, 30, fill = 'orange')

root.mainloop()
