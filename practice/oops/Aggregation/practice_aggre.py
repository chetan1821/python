class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show_student(self):
        print("Name : ",self.name)
        print("Age : ",self.age)

class School:
    def __init__(self):
        self.student=[]
    def add_student(self,student):
        self.student.append(student)
    def show_student(self):
        for i in self.student:
            i.show_student()

s1 = Student("Chetan",20)
s2 = Student("Rahul",21)

school = School()

school.add_student(s1)
school.add_student(s2)

school.show_student()