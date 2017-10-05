from aircraft import Aircraft, F16, F35

class Carrier():

    def __init__(self, ammo_stored = 600, health_point = 500):
        self.stored_crafts = []
        self.ammo_stored = ammo_stored
        self.health_point = health_point

    def add_aircraft(self, x):
        if x == self.aircraft.aircraft_type(x):
            self.stored_crafts.append (F16.status())
        elif x == self.aircraft.aircraft_type(x):
            self.stored_crafts.append (F35.status())
        return self.stored_crafts


        # return self.stored_crafts(aircraft_type.status(aircraft_type))


        



big_bill = Carrier()
print(big_bill.health_point)
big_bill.add_aircraft('F35')
print(big_bill.stored_crafts)
