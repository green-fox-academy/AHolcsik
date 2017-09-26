class Person:

    def __init__(self, name = "Jane Doe", age = "30", gender = "female"):
        self.name = name
        self.age = int(age)
        self.gender = gender

    def introduce(self):
        print("Hi, I'm {}, a {} year old {}".format(self.name, self.age, self.gender))

    def get_goal(self):
        print("My goal is: Live for the moment!")

class Student(Person):

    def __init__(self, name = "Jane Doe", age = "30", gender = "female", previous_organization = "The Shool of Life", skipped_days = 0):
        super().__init__()
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





stu = Student()
stu.introduce()


