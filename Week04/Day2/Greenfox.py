class Person:

    def __init__(self, name = "Jane Doe", age = "30", gender = "female"):
        self.name = name
        self.age = int(age)
        self.gender = gender

    def introduce(self):
        print("Hi, I'm {}, a {} year old {}".format(self.name, self.age, self.gender))

    def get_goal(self):
        print("My goal is: Live for the moment!")

class Student:

    def __init__(self, name = "Jane Doe", age = "30", gender = "female", previous_organization = "The Shool of Life", skipped_days = 0):
        self.name = name
        self.age = int(age)
        self.gender = gender
        self.previous_organization = previous_organization
        self.skipped_days = skipped_days

    def get_goal(self):
        print("Be a junior software developer.") 

    def introduce(self):
        print("Hi, I'm {}, a {} year old {} from {} who skipped {} days from the course already.".format(self.name, self.age, self.gender, self.previous_organization, self.skipped_days))

    def skipped_days(number_of_days):
        self.skipped_days += number_of_days

class Mentor:

    def __init__(self, name = "Jane Doe", age = "30", gender = "female", level = "intermediate"):
        self.name = name
        self.age = int(age)
        self.gender = gender
        self.level = level

    def get_goal(self):
        print("Educate brilliant junior software developers.")

    def introduce(self):
        print("Hi, I'm {}, a {} year old {} {} mentor".format(self.name, self.age, self.gender, self.level))




stu = Mentor()
stu.introduce()




