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
        x = 0
        y = 0
        self.hero = self.canvas.create_image(x + 36, y + 36, image = self.hero_down)

    def move(self, x, y):
        self.x += x
        self.y += y
        self.canvas.move(self.hero, x * 72, y * 72)

    def change_image(self, hero_image):
        self.hero_image = hero_image
        self.canvas.itemconfigure(self.hero, image = self.hero_image)


    # def change_image(self, direction):
    #     if direction == 'up':
    #         self.canvas.itemconfigure(self.hero_image, image = self.hero_up)
    #     if direction == 'down':
    #         self.canvas.itemconfigure(self.hero_image, image = self.hero_down)
    #     if direction == 'left':
    #         self.canvas.itemconfigure(self.hero_image, image = self.hero_left)
    #     if direction == 'right':
    #         self.canvas.itemconfigure(self.hero_image, image = self.hero_right)
