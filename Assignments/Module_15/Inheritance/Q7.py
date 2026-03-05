# Use of super() in Inheritance
class Parent:
    def __init__(self):
        print("Parent Constructor")

    def show(self):
        print("Parent Method")

class Child(Parent):
    def __init__(self):
        super().__init__()   # calling parent constructor
        print("Child Constructor")

    def display(self):
        super().show()       # calling parent method
        print("Child Method")

obj = Child()
obj.display()