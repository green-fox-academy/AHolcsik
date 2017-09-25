from fleet import Fleet
from thing import Thing

fleet = Fleet()

first = Thing(name = 'Get milk')
second = Thing(name = 'Remove the obstacles')
third = Thing(name = 'Stand up')
fourth = Thing(name = 'Eat lunch')

third.complete()
fourth.complete()

fleet.add(first)
fleet.add(second)
fleet.add(third)
fleet.add(fourth)

# Create a fleet of things to have this output:
# 1. [ ] Get milk
# 2. [ ] Remove the obstacles
# 3. [x] Stand up
# 4. [x] Eat lunch

print(fleet)
