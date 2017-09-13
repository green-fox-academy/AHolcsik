# Saturn is missing from the planet_list
# Insert it into the correct position

planet_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Uranus", "Neptune"]
addition = "Saturn"

planet_list = planet_list[:5] + [addition] + planet_list[6:]

print(planet_list)