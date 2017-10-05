from tkinter import *
# from view import 
# from entity import 

class Game(object):

    def __init__(self):
        root = Tk()
        canvas_height = 720
        canvas_width = 780
        canvas = Canvas(root, width=canvas_width, height=canvas_height)
        self.hero = Hero(canvas)
        # self.hero.draw(0, 0)
        self.skeleton = Skeleton(canvas)
        self.boss = Boss(canvas)
        # self.skeleton_number = 3
        # self.spots = self.map.create_enemy_spots(self.skeleton_number + 1)
        # self.skeleton.draw(self.spots[:-1])
        # self.boss.draw(self.spots[-1])

        def on_key_press(self, e):
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



        root.bind("<KeyPress>", self.on_key_press)
        canvas.pack()
        root.mainloop()













game = Game()