# Write a function that copies a file to an other
# It should take the filenames as parameters
# It should return a boolean that shows if the copy was successful

file_1 = "my-file.txt"
file_2 = "new.txt"

def copy_file(file_1, file_2):
    f = open (file_1, "r")
    fw = open (file_2, "r+")
    for line in f.readlines():
            fw.write(line)

copy_file(file_1, file_2)