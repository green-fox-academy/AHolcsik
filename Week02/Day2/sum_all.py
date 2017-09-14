# - Create a variable named `ai`
#   with the following content: `[3, 4, 5, 6, 7]`
# - Print the sum of the elements in `ai`

ai = [3, 4, 5, 6, 7]

def sum_all(ai):
    sum_ai = 0
    for element in (ai):
        sum_ai += element
    print(sum_ai)

sum_all(ai)
