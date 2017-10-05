from tkinter import *
from view import Map

class Entity():

    def __init__(self):
        self.x = 0
        self.y = 0

class Hero(Entity):

    def __init__(self, canvas):
        super(Hero, self).__init__()
        self.x = 0
        self.y = 0
        self.hero_image = None
        self.hero_down = PhotoImage(file = 'hero-down.gif')
        self.hero_up = PhotoImage(file = 'hero-up.gif')
        self.hero_left = PhotoImage(file = 'hero-left.gif')
        self.hero_right = PhotoImage(file = 'hero-right.gif')
        self.canvas = canvas

    def create_hero(self):
        x = 36
        y = 36
        self.hero = self.canvas.create_image(x, y, image = self.hero_down)

    def move(self, x, y):
        self.coord_x += x
        self.coord_y += y
        self.canvas.move(self.hero, x * size, y * size)

    def change_look(self, look):
        self.look = look
        self.canvas.itemconfigure(self.hero, image = self.hero_image)
