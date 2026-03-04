# What is Inheritance in Python?
# Inheritance is an OOP (Object-Oriented Programming) concept where a child class
#  (derived class) can use the properties and methods of another class (parent/base class).
# 
class vehicle:
    def __init__(self,name,flue_type):
        self.name=name
        self.flue_type=flue_type

    def display(self):
        print(self.name,self.flue_type)

class bike(vehicle):
    def __init__(self, name, flue_type,speed):
        self.speed = speed
        super().__init__(name, flue_type)
    def display(self):
        print(self.speed)
        super().display()
        

class bus(vehicle):
    pass

b= bike("ktm","petrol","140kmp")
b.display()

