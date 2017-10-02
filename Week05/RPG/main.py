from tkinter import *


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

class Hero_down:
    def __init__(self):
        self.hero = None

    def create_hero(self, x, y):
        self.hero = canvas.create_image(x, y, image = hero_down)

    def move(self, dx, dy):
        canvas.move(self.hero, dx, dy)

Hero = Hero_down()
Hero.create_hero(42, 42)

def on_key_press(e):
    if (e.keysym == 'Up'):
        Hero.move(0,-72)
    elif (e.keysym == 'Down'):
        Hero.move(0,72)
    elif (e.keysym == 'Left'):
        Hero.move(-72,0)  
    elif (e.keysym == 'Right'):
        Hero.move(72,0)


# place_hero(42, 42)

root.bind("<KeyPress>", on_key_press)




root.mainloop()
