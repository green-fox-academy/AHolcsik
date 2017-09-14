# Write a program that stores 3 sides of a cuboid as variables (doubles)
# The program should write the surface area and volume of the cuboid like:
# 
# Surface Area: 600
# Volume: 1000


def surface_area(x, y, z):
    surface_area = 2 * (x*y + x*z + y*z)
    return(surface_area)

def volume(x, y, z):
    volume = x*y*z
    return(volume)

print(surface_area(2, 3, 4))
print(volume (4, 2, 3))