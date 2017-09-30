from animal import Animal, Chicken, Cow
import random

class Farm():

    def __init__(self):
        self.animals = [Animal(42, 11), Animal(14, 44), Animal(22, 27)]
        self.empty_slots_2 = 17
        self.empty_slots_4 = 4

    def breed(self):
        if self.empty_slots <= 0:
            return self.animals
        else:
            self.animals.append(Animal())
            self.empty_slots -= 1
            return self.empty_slots

    def slaughter(self):
        self.hungrier = []
        for i in self.animals:
            self.hungrier.append(i.hunger)
        self.animals.remove(self.animals[self.hungrier.index(min(self.hungrier))])
        return self.animals


farm = Farm()
farm.breed()
print(farm.empty_slots)
farm.slaughter()
print(farm.empty_slots)






    # def __init__(self):
    #     self.animals = []
    #     self.empty_2_legs = [cow()]
    #     self.empty_4_legs = []

    # def add_new(self, animal):
    #     self.animals.append(animal)

    # def breed(self):



