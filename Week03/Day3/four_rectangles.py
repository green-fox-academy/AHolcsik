from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw four different size and color rectangles.

green_box = canvas.create_rectangle(23, 45, 79, 102, fill='green')
pink_box = canvas.create_rectangle(223, 75, 290, 2, fill='pink')
yellow_box = canvas.create_rectangle(178, 5, 159, 207, fill='yellow')
blue_box = canvas.create_rectangle(30, 245, 149, 190, fill='blue')

root.mainloop()
