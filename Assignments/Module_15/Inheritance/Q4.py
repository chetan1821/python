# Multiple Inheritance
class Father:
    def father_skill(self):
        print("Father skill")

class Mother:
    def mother_skill(self):
        print("Mother skill")

class Child(Father, Mother):
    def child_skill(self):
        print("Child skill")

obj = Child()
obj.father_skill()
obj.mother_skill()
obj.child_skill()