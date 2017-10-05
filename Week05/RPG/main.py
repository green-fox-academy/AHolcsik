from tkinter import *
from view import Map 
from entity import Hero, Skeleton

class Game(object):

    def __init__(self):
        root = Tk()
        canvas_height = 720
        canvas_width = 780
        canvas = Canvas(root, width=canvas_width, height=canvas_height)
        self.map = Map()
        self.map.draw_map(canvas)
        self.hero = Hero(canvas)
        self.hero.create_hero()
        self.skeleton = Skeleton(canvas)
        self.skeleton_number = 3
        self.spawn_spots = self.map.create_spawn_spots(self.skeleton_number)
        self.skeleton.spawn_skeleton(self.spawn_spots[:-1])
    
        root.bind("<KeyPress>", self.on_key_press)
        canvas.pack(padx = 1, pady = 0.6)
        root.mainloop()

    def on_key_press(self, e):
        if (e.keysym == 'Up'):
            self.hero.change_image(self.hero.hero_up)
            if self.map.is_in_border_floor(self.hero.x, self.hero.y - 1) == True:
                self.hero.move(0,-1)
        elif (e.keysym == 'Down'):
            self.hero.change_image(self.hero.hero_down)
            if self.map.is_in_border_floor(self.hero.x, self.hero.y + 1) == True:
                self.hero.move(0,1)
        elif (e.keysym == 'Left'):
            self.hero.change_image(self.hero.hero_left)
            if self.map.is_in_border_floor(self.hero.x - 1, self.hero.y) == True:
                self.hero.move(-1,0)
        elif (e.keysym == 'Right'):
            self.hero.change_image(self.hero.hero_right)
            if self.map.is_in_border_floor(self.hero.x + 1, self.hero.y) == True:
                self.hero.move(1,0)




        
        





    


game = Game()