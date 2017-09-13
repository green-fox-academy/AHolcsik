# Join the two lists by matching one girl with one boy in the order list
# Exepected output: ["Eve", "Joe", "Ashley", "Fred"...]

girls = ["Eve", "Ashley", "Bozsi", "Kat", "Jane"]
boys = ["Joe", "Fred", "Bela", "Todd", "Neef", "Jeff"]

def matching(girls, boys):
    order = []
    for i in (boys):
        for j in (girls):
            order.append (i)
#        if i < len(boys):
            
            order.append (j)
        else:
            print (order)
    return (order)

print(matching(girls,boys))
  