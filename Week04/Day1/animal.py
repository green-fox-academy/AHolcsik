# Create Animal class
# Every animal has a hunger value, which is a whole number
# Every animal has a thirst value, which is a whole number
# when creating a new animal object these values are created with the default 50 value
# Every animal can eat() which decreases their hunger by one
# Every animal can drink() which decreases their thirst by one
# Every animal can play() which increases both by one

class Animal(object):

    def __init__(self):
        self.hunger = int(50)
        self.thirst = int(50)

    def eat(self):
        self.hunger -= 1
        print('om nom nom')

    def drink(self):
        self.thirst -=1

    def play(self):
        self.hunger -= 1
        self.thirst -= 1

cat = Animal()
cat.play()
cat.play()
cat.eat()
print(cat.hunger, cat.thirst)