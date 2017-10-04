from tkinter import *
import random


root = Tk()
canvas = Canvas(root, width = 800, height = 800)
canvas.pack()
canvas.focus_set()

floor = PhotoImage(file = 'floor.gif')
wall = PhotoImage(file = 'wall.gif')
hero_down = PhotoImage(file = 'hero-down.gif')
hero_up = PhotoImage(file = 'hero-up.gif')
hero_left = PhotoImage(file = 'hero-left.gif')
hero_right = PhotoImage(file = 'hero-right.gif')
boss = PhotoImage(file = 'boss.gif')
skeleton = PhotoImage(file = 'skeleton.gif')


def floor_piece(x, y, size):
    floo = canvas.create_image(x * size, y * size, image = floor)

def wall_piece(x, y, size):
    woo = canvas.create_image(x * size, y * size, image = wall)

def draw_whole_map(map_layout, size):
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
              [0,1,1,1,0,0,0,0,0,0],
              ]

def is_in_border_floor(x, y):
    if 0 <= x <= 9 and 0 <= y <= 8:
        if map_layout[y][x] == 0:
            return True


size = 72
draw_whole_map(map_layout, size)

class Hero:

    def __init__(self):
        self.coord_x = 0
        self.coord_y = 0
        self.look = hero_down

    def create_hero(self):
        x = 42
        y = 42
        self.hero = canvas.create_image(x, y, image = self.look)

    def move(self, x, y):
        self.coord_x += x
        self.coord_y += y
        canvas.move(self.hero, x * size, y * size)

    def change_look(self, look):
        self.look = look
        canvas.itemconfigure(self.hero, image = self.look)


Hero = Hero()
Hero.create_hero()

def on_key_press(e):
        if (e.keysym == 'Up') and is_in_border_floor(Hero.coord_x, Hero.coord_y -1) == True:
            Hero.move(0,-1)
            Hero.look = hero_up
            Hero.change_look(hero_up)
        elif (e.keysym == 'Down') and is_in_border_floor(Hero.coord_x, Hero.coord_y +1) == True:
            Hero.move(0,1)
            Hero.look = hero_down
            Hero.change_look(hero_down)
        elif (e.keysym == 'Left') and is_in_border_floor(Hero.coord_x -1, Hero.coord_y) == True:
            Hero.move(-1,0)
            Hero.look = hero_left
            Hero.change_look(hero_left)  
        elif (e.keysym == 'Right') and is_in_border_floor(Hero.coord_x +1, Hero.coord_y) == True:
            Hero.move(1,0)
            Hero.look = hero_right
            Hero.change_look(hero_right)

class Skeleton():

    def __init__(self):
        self.image = skeleton

    def create_skeleton(self):
        random_x = random.randint(0,9)
        random_y = random.randint(0,8)
        if is_in_border_floor(random_x, random_y) == True:
            x = 42 + size * random_x
            y = 42 + size * random_y
            self.skeleton = canvas.create_image(x, y, image = self.image)
        else:
            self.create_skeleton()
        



    # def move(self, x, y):
    #     self.coord_x += x
    #     self.coord_y += y
    #     canvas.move(self.hero, x * size, y * size)


skeleton = Skeleton()
skeleton.create_skeleton()

root.bind("<KeyPress>", on_key_press)

root.mainloop()
