# Create Animal class
# Every animal has a hunger value, which is a whole number
# Every animal has a thirst value, which is a whole number
# when creating a new animal object these values are created with the default 50 value
# Every animal can eat() which decreases their hunger by one
# Every animal can drink() which decreases their thirst by one
# Every animal can play() which increases both by one

class Animal():

    def __init__(self, hunger = 50, thirst = 50, happiness = 50):
        self.hunger = hunger
        self.thirst = thirst
        self.happiness = happiness

    def eat(self):
        self.hunger -= 1

    def drink(self):
        self.thirst -=1

    def play(self):
        self.hunger -= 2
        self.thirst -= 2
        self.happiness += 1

class Chicken(Animal):

    def __init__(self, hunger = 50, thirst = 50, happiness = 50):
        super().__init__(hunger, thirst, happiness)

    def lay_egg(self):
        pass

class Cow(Animal):

    def __init__(self, hunger = 50, thirst = 50, happiness = 50):
        super().__init__(hunger, thirst, happiness)

    def produce_milk(self):
        pass


chick = Chicken()
chick.lay_egg


print(chick.happiness)