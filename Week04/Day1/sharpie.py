# Create Sharpie class
# We should know about each sharpie their color (which should be a string), width (which will be a floating point number), ink_amount (another floating point number)
# When creating one, we need to specify the color and the width
# Every sharpie is created with a default 100 as ink_amount
# We can use() the sharpie objects
# which decreases inkAmount

class Sharpie(object):
    ink_amount = int(100)

    def __init__(self, color, width):
        self.color = color
        self.width = float(width)

    def use(self):
        self.ink_amount -= 1 * self.width

blue = Sharpie(color = 'Blue', width = '0.5')
red = Sharpie(color = 'Red', width = '1')
purple = Sharpie(color = 'Violet', width = '10')

blue.use()
red.use()
purple.use()
purple.use()
print('Red has', red.ink_amount, 'units left')
print('Blue has', blue.ink_amount, 'units left')
print('Purple has', purple.ink_amount, 'units left')