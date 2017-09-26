class Garden:

    def __init__(self):
        self.plants = []

    def add(self, element):
        if element in self.plants:
            pass
        else:
            self.plants.append(element)

    # def __str__(self):


    def water(self, amount, plants):
        for element in plants:
            if element.needs_water():
                element.water_amount += (amount / len(plants)) * 0.75

class Plant:

    def __init__(self, water_amount, color):
        self.color = color
        self.water_amount = water_amount

    def needs_water(self):
        if self.water_amount < 5:
            return 'needs water'
        else:
            return 'not needs water'

orange_tree = Plant(water_amount = 4, color = "orange")
purple_tree = Plant(water_amount = 5, color = "purple")
yellow_flower = Plant(water_amount = 1, color = "yellow")
blue_flower = Plant(water_amount = 3, color = "blue")

garden = Garden()

garden.add(yellow_flower)
garden.add(blue_flower)
garden.add(orange_tree)
garden.add(purple_tree)
print(garden.plants)

for member in garden.plants:
    print(member.needs_water())

garden.water(10, garden.plants)

for member in garden.plants:
    print(member.water_amount)