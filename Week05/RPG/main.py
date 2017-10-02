from tkinter import *


root = Tk()
canvas = Canvas(root, width = 1000, height = 1000)
canvas.pack()

floor = PhotoImage(file = 'floor.gif')
canvas.create_image(10, 10, image = floor)





root.mainloop()
