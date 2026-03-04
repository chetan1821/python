# 1
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# class student(person):
#     def display(self):
#         print(self.name)
#         print(self.age)

# s= student("chetan",20)
# s.display()

# 2
# class Vehicle:
#     def __init__(self):
#         pass
#     def start(self):
#         print("car started")

# class car(Vehicle):
#     def __init__(self):
#         super().__init__()
        
#     def start(self):
#         super().start()
        

# c =car()
# c.start()

# 3
# class Animal:
    
#     def eat(self):
#         print("its eat somthing..")
    
# class Dog(Animal):
#     def bark(self):
#         print("booo booo")
    
# d = Dog()
# d.eat()
# d.bark()


# 4 
# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary

# class Manager(Employee):
#     def __init__(self, name, salary,department):
#         self.department=department
#         super().__init__(name, salary)

#     def display_info(self):
#         print(self.name)
#         print(self.salary)
#         print(self.department)

# m = Manager("chetan",12000,"SE")
# m.display_info()

# 5
class Shape:
   def area(self):
       print("Area of shape")

class Circal(Shape):
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        area = 3.14 * self.radius * self.radius
        print("Area of Circle:", area)
        
c=Circal(5)
c.area()


        
        



        



