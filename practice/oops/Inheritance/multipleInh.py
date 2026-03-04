# Multiple Inheritance
class Person:
    def __init__(self,name):
        self.name=name

class Student:
    def __init__(self,roll_no):
        self.roll_no=roll_no

class CollageStudent(Person,Student):
    def __init__(self, name,roll_no,course):
        self.course=course
        Person.__init__(self,name)
        Student.__init__(self,roll_no)

    def display(self):
        print(self.roll_no,self.name,self.course)

c = CollageStudent("chetan",644,"BCA")
c.display()
        
        