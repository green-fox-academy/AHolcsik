# Join the two lists by matching one girl with one boy in the order list
# Exepected output: ["Eve", "Joe", "Ashley", "Fred"...]

girls = ["Eve", "Ashley", "Bozsi", "Kat", "Jane"]
boys = ["Joe", "Fred", "Bela", "Todd", "Neef", "Jeff"]

def matching(girls, boys):
    order = boys
    a = 0
    for i in (girls):
            order.insert (a,i)
            a += 2
    print (order)
    return (order)

matching(girls,boys)
  