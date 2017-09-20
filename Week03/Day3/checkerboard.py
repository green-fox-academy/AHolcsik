from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# fill the canvas with a checkerboard pattern.

board_width = 8

def checkerboard(board_width):
    size = 30
    x = 30
    y = 30
    for i in range(board_width):
        for j in range(board_width):
            if (i + j) % 2 == 0:
                tile = canvas.create_rectangle(x + (i * size), y + (j * size), 2 * x + (i * size), 2 * y + (j * size), fill='black')
            else:
                tile = canvas.create_rectangle(x + (i * size), y + (j * size), 2 * x + (i * size), 2 * y + (j * size), fill='white')

checkerboard(board_width)

root.mainloop()
