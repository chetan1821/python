# inheritance is process that access the property of one class to another classs
# Base class => child class

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(self.name,self.age)

# class student(person):
#     def __init__(self, id,name, age,standard,dob):
#         self.id=id
#         self.standard=standard
#         self.dob=dob
#         super().__init__(name, age)

#     def display(self):
#         super().display()
#         print(self.id,self.standard,self.dob)

# s = student("10","chetan",20,"10th","12/08/2005")
# s.display()

class A:
    name = "chetan"
    print("hello this ")
class B(A):
    # print(name)
    print("class b")

b=B()


