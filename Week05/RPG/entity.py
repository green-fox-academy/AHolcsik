from tkinter import *
from view import Map
import random

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

class Skeleton(Entity):

    def __init__(self, canvas):
        super(Skeleton, self).__init__()
        self.x = 0
        self.y = 0
        self.skeleton = PhotoImage(file = 'skeleton.gif')
        self.canvas = canvas

    def spawn_skeleton(self, spawn_spots):
        for i in range(len(spawn_spots)):
            self.skeleton = self.canvas.create_image(spawn_spots[i][0], spawn_spots[i][1], image = self.skeleton)

