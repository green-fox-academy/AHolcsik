from tkinter import *

root = Tk()

canvas = Canvas(root, width='500', height='500', bg='yellow')
canvas.pack()

def triangles(level, x0, y0, x1, y1, x2, y2):
    if level <= 0:
        return canvas.create_polygon(x0, y0, x1, y1, x2, x2, fill='green')
    else:
        triangles(level-1,
                       x0, y0,
                       (x0+x1)/2, (y0+y1)/2,
                       (x0+x2)/2, (y0+y2)/2)
        # lower left triangle
        triangles(level-1,
                       (x0+x1)/2, (y0+y1)/2,
                       x1, y1,
                       (x1+x2)/2, (y1+y2)/2)
        # lower right triangle
        triangles(level-1,
                       (x0+x2)/2, (y0+y2)/2,
                       (x1+x2)/2, (y1+y2)/2,
                       x2, y2)

print(triangles(3, 0, 500, 250, 0, 500, 500))

    

root.mainloop()