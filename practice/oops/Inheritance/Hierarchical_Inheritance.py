# Hierarchical Inheritance
# HI means multiple child classes inherit from a singal parent class.
class person:
    def __init__(self,name):
        self.name=name
    def show_name(self):
        print("name : ",self.name)

class student(person):
    def study(self):
        print("name of student : ",self.name)

class Teacher(person):
    def tech(self):
        print("Teacher name : ",self.name)

s= student("chetan")
t=Teacher("chintan sir")

s.show_name()
s.study()
t.show_name()
t.tech()

# ***************************************************
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary

    def show_employee(self):
        self.show_person()
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course

    def show_student(self):
        self.show_person()
        print("Roll No:", self.roll_no)
        print("Course:", self.course)


class Customer(Person):
    def __init__(self, name, age, customer_id, purchase_amount):
        super().__init__(name, age)
        self.customer_id = customer_id
        self.purchase_amount = purchase_amount

    def show_customer(self):
        self.show_person()
        print("Customer ID:", self.customer_id)
        print("Purchase Amount:", self.purchase_amount)


# Objects
e = Employee("Chetan", 20, 101, 30000)
s = Student("Rahul", 19, 12, "BCA")
c = Customer("Amit", 30, 501, 1500)

e.show_employee()
print("-----")
s.show_student()
print("-----")
c.show_customer()


# **************************************************
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary

    def show_details(self):
        self.show_person()
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course

    def show_details(self):
        self.show_person()
        print("Roll No:", self.roll_no)
        print("Course:", self.course)


class Customer(Person):
    def __init__(self, name, age, customer_id, purchase_amount):
        super().__init__(name, age)
        self.customer_id = customer_id
        self.purchase_amount = purchase_amount

    def show_details(self):
        self.show_person()
        print("Customer ID:", self.customer_id)
        print("Purchase Amount:", self.purchase_amount)


# 🔽 Dynamic Input
choice = input("Enter type (employee / student / customer): ").lower()

name = input("Enter name: ")
age = int(input("Enter age: "))

if choice == "employee":
    emp_id = input("Enter employee id: ")
    salary = float(input("Enter salary: "))
    obj = Employee(name, age, emp_id, salary)

elif choice == "student":
    roll_no = input("Enter roll number: ")
    course = input("Enter course: ")
    obj = Student(name, age, roll_no, course)

elif choice == "customer":
    customer_id = input("Enter customer id: ")
    purchase_amount = float(input("Enter purchase amount: "))
    obj = Customer(name, age, customer_id, purchase_amount)

else:
    print("Invalid choice")
    obj = None

# 🔽 Display details
if obj:
    print("\n--- Details ---")
    obj.show_details()


