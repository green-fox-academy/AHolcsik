# Create a class, with one method (eg. get_apple()) that returns a string (eg. "apple")
# Create a test for that:
# Create a test class
# Create a test method
# Instantiate an Object from your class in the method
# Use the assertEquals()
# The expected parameter should be the same string (eg. "apple")
# The actual parameter should be the return value of the method (eg. myobject.get_apple())
# Run the test
# Change the expected value to make the test failing
# Run the test
# Fix the returned value to make the test succeeding again

class GetsApple:

    def get_apple(self):
        return "apple"


# Create a sum method in your class which has a list of integers as parameter
# It should return the sum of the elements in the list
# Follow these steps:
# Add a new test case
# Instantiate your class
# create a list of integers
# use the assertEquals to test the result of the created sum method
# Run it
# Create different tests where you
# test your method with an empyt list
# with a list with one element in it
# with multiple elements in it
# with a null
# Run them
# Fix your code if needed

class SumExercise:

    def sum_numbers(self, list):
        output = 0
        for element in list:
            output += element
        return output
        
# Write a function, that takes two strings and returns a boolean value based on if the two strings are Anagramms or not.
# Create a test for that.

class Anagramm:

    def is_anagramm(self, text1, text2):
        if len(text1) == len(text2):
            list_of_letters = []
            for letter in text1:
                list_of_letters.append(letter)
            for letter in text2:
                if letter in list_of_letters:
                    list_of_letters.remove(letter)
                if len(list_of_letters) == 0:
                    return True
        return False

# Write a function, that takes a string as an argument and returns a dictionary with all letters in the string as keys, and numbers as values that shows how many occurrences there are.
# Create a test for that.

class CountLetters:

    def number_of_letters(self, string):
        return

