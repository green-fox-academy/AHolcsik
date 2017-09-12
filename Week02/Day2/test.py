def greet_by_name(name):
  print("Well hi there,", name)

greet_by_name("Tojas")
greet_by_name("Barbi")

def make_green(name):
  new_name = "Green " + name
  return new_name

name = make_green("Tojas")
greet_by_name(name)