import random

class Dice(object):

    def __init__(self):
        self.dice = [0, 0, 0, 0, 0, 0]

    def roll(self):
        for i in range(len(self.dice)):
            self.dice[i] = random.randint(1,6)
        return self.dice

    def get_current(self, index=None):
        if index != None:
            return self.dice[index]
        else:
            return self.dice

    def reroll(self, index=None):
        if index != None:
            self.dice[index] = random.randint(1,6)
        else:
            self.roll()

# dice.reroll(3)
# print(dice.get_current(3))


dice = Dice()
print(dice.get_current())
dice.roll()
result = dice.get_current()
print(result)
for element in range(len(result)):
    while dice.get_current(element) != 6:
        dice.reroll(element)

print(dice.get_current())
