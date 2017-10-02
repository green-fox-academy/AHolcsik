from tkinter import *


root = Tk()
canvas = Canvas(root, width = 800, height = 800)
canvas.pack()

floor = PhotoImage(file = 'floor.gif')
wall = PhotoImage(file = 'wall.gif')

def floor_piece(x, y, size):
    floo = canvas.create_image(x * size, y * size, image = floor)

def wall_piece(x, y, size):
    woo = canvas.create_image(x * size, y * size, image = wall)

def draw_whole_map(map_layout, x, y, size):
    for column in range(len(map_layout)):
        for row in range(len(map_layout[0])):
            if map_layout[column][row] == 0:
                floor_piece(row + 0.6, column + 0.6, size)
            elif map_layout[column][row] == 1:
                wall_piece(row + 0.6, column + 0.6, size)

map_layout = [[0,0,0,1,0,1,0,0,0,0],
              [0,0,0,1,0,1,0,1,1,0],
              [0,1,1,1,0,1,0,1,1,0],
              [0,0,0,0,0,1,0,0,0,0],
              [1,1,1,1,0,1,1,1,1,0],
              [0,1,0,1,0,0,0,0,1,0],
              [0,1,0,1,0,1,1,0,1,0],
              [0,0,0,0,0,1,1,0,1,0],
              [0,1,1,1,0,0,0,0,1,0],
              [0,0,0,1,0,1,1,0,1,0],
              [0,1,0,1,0,1,0,0,0,0]
              ]

draw_whole_map(map_layout, 72, 72, 72)

root.mainloop()
