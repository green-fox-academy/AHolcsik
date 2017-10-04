
class Aircraft():
    def __init__(self, ammo, base_damage, damage):
        self.ammo = 0
        self.base_damage = base_damage
        self.damage = damage

    def fight(self):
        pew_pew = self.ammo * self.base_damage
        self.ammo = 0
        return pew_pew

    def refill(self, number):
        difference = self.max_ammo - self.ammo
        self.ammo += difference
        return (number - difference)

    def get_type(self):
        return self.type

    def status(self):
        return 'Type: ' + self.type + ', Ammo: ' + str(self.ammo) + ', Base Damage: ' + str(self.base_damage) + ', All Damage: ' + str(self.fight())


class F16 (Aircraft):

    def __init__(self, ammo, damage = 0, max_ammo = 8, base_damage = 30, type = 'F16'):
        super().__init__(self, ammo, damage)
        self.max_ammo = max_ammo
        self.base_damage = base_damage
        self.damage = damage
        self.type = type

class F35 (Aircraft):
    def __init__(self, ammo, damage = 0, max_ammo = 12, base_damage = 50, type = 'F35'):
        super().__init__(self, ammo, damage)
        self.max_ammo = max_ammo
        self.base_damage = base_damage
        self.damage = damage
        self.type = type
        
pityu = F35(Aircraft)
lil_g = F16(Aircraft)
print(pityu.fight())
print(pityu.refill(200))
print(pityu.status())







