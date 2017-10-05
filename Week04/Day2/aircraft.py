
class Aircraft():
    def __init__(self, max_ammo, base_damage, aircraft_type):
        self.max_ammo = max_ammo
        self.aircraft_type = aircraft_type
        self.ammo = 0
        self.base_damage = base_damage


    def fight(self):
        pew_pew = self.ammo * self.base_damage
        self.ammo = 0
        return pew_pew

    def refill(self, number):
        difference = self.max_ammo - self.ammo
        self.ammo += difference
        return (number - difference)

    def get_type(self):
        return self.aircraft_type

    def status(self):
        return 'Type: ' + self.aircraft_type + ', Ammo: ' + str(self.ammo) + ', Base Damage: ' + str(self.base_damage) + ', All Damage: ' + str(self.fight())


class F16 (Aircraft):

    def __init__(self):
        super(F16, self).__init__(8, 30, 'F16')
        

class F35 (Aircraft):
    def __init__(self):
        super(F35, self).__init__(12, 50, 'F35')

        
pityu = F35()
lil_g = F16()
print(pityu.fight())
print(pityu.refill(200))
print(pityu.status())







