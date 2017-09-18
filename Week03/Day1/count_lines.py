# Write a function that takes a filename as string,
# then returns the number of lines the file contains.
# It should return zero if it can't open the file, and
# should not raise any error.

file_name = "my-file.txt"

def lines(file_name):
    try:
        number_of_lines = 0
        f = open(file_name, "r")
        for line in f:
            number_of_lines += 1
        print(number_of_lines)
    except IOError:
        print(0)
    
lines(file_name)


