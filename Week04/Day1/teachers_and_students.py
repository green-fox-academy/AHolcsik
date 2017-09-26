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

    def question(self, teacher):
        teacher.teach
        print('wtf?')


class Teacher(object):

    def teach(self, student):
        student.learn
        print('bla bla bla')

Jolanka = Teacher()
Pistike = Student()
Pistike.question(Jolanka)
Jolanka.teach(Pistike)


