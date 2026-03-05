# Global variable
college = "Bhagwan Mahavir University"

class Student:

    def show(self):
        # Local variable
        name = "Chetan"

        print("Local variable (Name):", name)
        print("Global variable (College):", college)


# Object creation
s1 = Student()
s1.show()