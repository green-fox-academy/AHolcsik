from aircraft import Aircraft, F16, F35

class Carrier():

    def __init__(self, ammo_stored = 600, health_point = 500):
        self.stored_crafts = []
        self.ammo_stored = ammo_stored
        self.health_point = health_point

    def add_aircraft(self, aircraft_type):
        self.stored_crafts.append(Aircraft(aircraft_type, 0, 0))

    def fill(self):
        if self.ammo == 0:
            return 'No ammo!'
        for aircraft in self.stored_crafts:
            if aircraft.aircraft_type == 'F35':
                self.ammo = aircraft.refill(self.ammo)
        for aircraft in self.stored_crafts:
            if aircraft.aircraft_type == 'F16':
                self.ammo = aircraft.refill(self.ammo)

    def get_status(self):
        sum_of_damage = 0
        for aircraft in self.stored_crafts:
            sum_of_damage += aircraft.base_damage * aircraft.ammo
            base_status = "HP: " + str(self.health_point) +", Aircraft count: "+ str(len(self.stored_crafts)) +", Ammo Storage: " + str(self.ammo_stored) + ", Total damage: " + str(sum_of_damage)
            base_status += "Aircrafts: \n"
        for aircraft in self.stored_crafts:
            base_status += aircraft.status() + "\n"
        return base_status
        

big_bill = Carrier()
print(big_bill.health_point)
big_bill.add_aircraft('F35')
big_bill.add_aircraft('F35')
big_bill.add_aircraft('F16')
print(big_bill.get_status())
big_bill.fill()
print(big_bill.stored_crafts)
