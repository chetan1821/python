# multilevel Inheritance1
# class A:
#     print("This is A")
# class B(A):
#     print("This is B")
# class C(B):
#     pass

# c1 =C()

# class A:
#     def fetutre_1(self):
#         print("This is A Feature")

# class B(A):
#     def fetutre_2(self):
#         print("This is B Feature")

# class C(B):
#     def fetutre_3(self):
#         print("this is c Feature")

# c=C()
# c.fetutre_1()
# c.fetutre_2()
# c.fetutre_3()


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_person(self):
        print("Name : ",self.name)
        print("Age :- ",self.age)

class Employee(Person):
    def __init__(self, name, age,emp_id,salary):
        self.emp_id=emp_id
        self.salary=salary
        super().__init__(name, age)

    def display_employee(self):
        self.display_person()
        print("Emp_id : ",self.emp_id)
        print("Emp_salary : ",self.salary)

class Manager(Employee):
    def __init__(self, name, age, emp_id, salary,department,bonus):
        self.department=department
        self.bonus=bonus
        super().__init__(name, age, emp_id, salary)

    def display_manager(self):
        self.display_employee()
       
        total = self.salary+self.bonus
        print("Emp_Department : ",self.department)
        print("Emp_Bonus :",self.bonus)
        print("Total salary :",total)

        if total > 50000:
            print("High level")
        else:
            print("Mid level")

m =Manager("chetan",20,1,50000,"IT",500)
m.display_manager()

