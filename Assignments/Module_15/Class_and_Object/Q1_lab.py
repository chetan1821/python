# Create a class

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


# Create object
s1 = Student("Chetan", 20, "BCA")

# Access properties using object
print(s1.name)
print(s1.age)
print(s1.course)

# Call method
s1.display()