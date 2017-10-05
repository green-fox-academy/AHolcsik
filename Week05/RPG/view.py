from tkinter import *

class Map():

    def __init__(self):
        self.floor_tile = floor = PhotoImage(file = 'floor.gif')
        self.wall_tile = wall = PhotoImage(file = 'wall.gif')
        self.tile_size = 72
        self.x = 0
        self.y = 0
        self.map_layout = [[0,0,0,1,0,1,0,0,0,0],
                           [0,0,0,1,0,1,0,1,1,0],
                           [0,1,1,1,0,1,0,1,1,0],
                           [0,0,0,0,0,1,0,0,0,0],
                           [1,1,1,1,0,1,1,1,1,0],
                           [0,1,0,1,0,0,0,0,1,0],
                           [0,1,0,1,0,1,1,0,1,0],
                           [0,0,0,0,0,1,1,0,1,0],
                           [0,1,1,1,0,0,0,0,0,0],
                           ]

    def draw_map(self, canvas):
        for i, line in enumerate(self.map_layout):
            for j, value in enumerate(line):
                if str(value) == '0':
                    canvas.create_image(self.tile_size / 2 + j * self.tile_size, self.tile_size / 2 + i * self.tile_size, image = self.floor_tile)
                elif str(value) == '1':
                    canvas.create_image(self.tile_size / 2 + j * self.tile_size, self.tile_size / 2 + i * self.tile_size, image = self.wall_tile)     

    def is_in_border_floor(self, x, y):
        if 0 <= x <= 9 and 0 <= y <= 8:
            if self.map_layout[y][x] == 0:
                return True
       