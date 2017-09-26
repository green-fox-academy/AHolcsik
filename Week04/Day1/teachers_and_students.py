# Create Student and Teacher classes
# Student
# learn()
# question(teacher) -> calls the teachers answer method
# Teacher
# teach(student) -> calls the students learn method
# answer()

class Student(object):

    def learn(self):
        print('oh wow')

    def question(teacher):
        teacher.teach
        print('wtf?')


class Teacher(object):

    def teach(student):
        student.learn
        print('bla bla bla')

Pistike = Student()
Pistike.question()

