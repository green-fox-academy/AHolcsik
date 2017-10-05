from tkinter import *

class Map(Object):

    def __init__(self):
        self.floor_tile = floor = PhotoImage(file = 'floor.gif')
        self.wall_tile = wall = PhotoImage(file = 'wall.gif')
        self.tile_size = 72
        self.x = 0
        self.x = 0
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

        # def floor_piece(x, y, size):
        #     floo = canvas.create_image(x * self.size, y * self.size, self.image = floor)

        # def wall_piece(x, y, size):
        #     woo = canvas.create_image(x * size, y * size, image = wall)

        def draw_map(self, canvas):
            for column in range(len(self.map_layout)):
                for row in range(len(self.map_layout[0])):
                    if self.map_layout[column][row] == 0:
                        canvas.create_image(x * self.size, y * self.size, image = self.floor_tile)
                    elif map_layout[column][row] == 1:
                        canvas.create_image(x * self.size, y * self.size, image = self.wall_tile)
        




# def is_in_border_floor(x, y):
#     if 0 <= x <= 9 and 0 <= y <= 8:
#         if map_layout[y][x] == 0:
#             return True

draw_whole_map(canvas)        