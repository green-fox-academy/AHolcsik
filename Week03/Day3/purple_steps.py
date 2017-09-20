from tkinter import *

root = Tk()

canvas = Canvas(root)
canvas.pack()
canvas_width = 300
canvas_height = 300

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps/r3.png]


nsteps = 20
step_x = int(canvas_width / nsteps)
step_y = int(canvas_height / nsteps)

for i in range(1, nsteps):
    purple_square = canvas.create_rectangle(0+(i*10), 0+(i*10), 10+(i*10), 10+(i*10), fill='purple')



root.mainloop()
