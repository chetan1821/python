# Hierarchical Inheritance
class Parent:
    def show(self):
        print("Parent class")

class Child1(Parent):
    def c1(self):
        print("Child1 class")

class Child2(Parent):
    def c2(self):
        print("Child2 class")

obj1 = Child1()
obj2 = Child2()

obj1.show()
obj1.c1()

obj2.show()
obj2.c2()