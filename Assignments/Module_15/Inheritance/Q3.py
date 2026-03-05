# Multilevel Inheritance
class Grandparent:
    def gp(self):
        print("Grandparent class")

class Parent(Grandparent):
    def p(self):
        print("Parent class")

class Child(Parent):
    def c(self):
        print("Child class")

obj = Child()
obj.gp()
obj.p()
obj.c()