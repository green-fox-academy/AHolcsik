# Create a program that prints all the even numbers between 0 and 500

number = list(range(0, 501))

def print_even(number):
    evens = []
    for i in number:
        if i % 2 == 0:
            evens.append (i)
    print(evens)

print_even(number)
