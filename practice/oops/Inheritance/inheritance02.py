class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

    def age_category(self):
        if self.age < 18:
            return "Minor"
        elif self.age <= 60:
            return "Adult"
        else:
            return "Senior"


class Student(Person):
    def __init__(self, sid, name, age, standard, dob):
        super().__init__(name, age)
        self.sid = sid
        self.standard = standard
        self.dob = dob

    def update_standard(self, new_standard):
        self.standard = new_standard
        print("Standard updated to", self.standard)

    def get_details(self):
        return {
            "ID": self.sid,
            "Name": self.name,
            "Age": self.age,
            "Standard": self.standard,
            "DOB": self.dob,
            "Category": self.age_category()
        }

    def __str__(self):
        return f"{self.sid} - {self.name} ({self.standard})"


# Object
s = Student("10", "Chetan", 20, "10th", "12/08/2005")

s.display()
print("Category:", s.age_category())

print("\nStudent Details:", s.get_details())

print("\nObject Print:", s)

# s.update_standard("11th")
