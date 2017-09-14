# - Create a variable named `abc`
#   with the following content: `["first", "second", "third"]`
# - Swap the first and the third element of `abc`

abc = ["first", "second", "third"]

a, b = abc.index ("first"), abc.index("third")
abc[a], abc[b] = abc[b], abc[a]
print(abc)
