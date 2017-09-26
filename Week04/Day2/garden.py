class Garden:

    def water(self, amount, plant, plants):
        for element in plants:
            if element.needs_water:
                element.water_amount += (amount / len(plants)) * 0.75


class Plant:

    def __init__(self, water_amount, color):
        self.color = color
        self.water_amount = water_amount

    def needs_water(self, water_amount):
        if self.water_amount < 5:
            return True


orange_tree = Plant(water_amount = 9, color = "orange")
purple_tree = Plant(water_amount = 5, color = "purple")
yellow_flower = Plant(water_amount = 1, color = "yellow")
blue_flower = Plant(water_amount = 6, color = "blue")

plants = []

plants.append(orange_tree)
plants.append(purple_tree)
plants.append(yellow_flower)
plants.append(blue_flower)

garden = Garden()

for member in plants:
    print(member.water_amount)

garden.water(10, blue_flower, plants)

for member in plants:
    print(member.water_amount)