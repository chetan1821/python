# ALL TYPES OF INHERITANCE DEMO

# 🔹 Base Class
class Person:
    def show_person(self):
        print("I am a Person")


# 1️⃣ Single Inheritance
class Student(Person):
    def show_student(self):
        print("I am a Student")

print("\n--- Single Inheritance ---")
s = Student()
s.show_person()
s.show_student()


# 2️⃣ Multilevel Inheritance
class CollegeStudent(Student):
    def show_college(self):
        print("I am a College Student")

print("\n--- Multilevel Inheritance ---")
cs = CollegeStudent()
cs.show_person()
cs.show_student()
cs.show_college()


# 3️⃣ Multiple Inheritance
class Sports:
    def show_sports(self):
        print("I play Sports")

class Result(Student, Sports):
    def show_result(self):
        print("I have Result")

print("\n--- Multiple Inheritance ---")
r = Result()
r.show_person()
r.show_student()
r.show_sports()
r.show_result()


# 4️⃣ Hierarchical Inheritance
class Teacher(Person):
    def show_teacher(self):
        print("I am a Teacher")

class Staff(Person):
    def show_staff(self):
        print("I am Staff")

print("\n--- Hierarchical Inheritance ---")
t = Teacher()
st = Staff()

t.show_person()
t.show_teacher()

st.show_person()
st.show_staff()


# 5️⃣ Hybrid Inheritance
class A:
    def show_a(self):
        print("Class A")

class B(A):
    def show_b(self):
        print("Class B")

class C(A):
    def show_c(self):
        print("Class C")

class D(B, C):   # Hybrid inheritance
    def show_d(self):
        print("Class D")

print("\n--- Hybrid Inheritance ---")
d = D()
d.show_a()
d.show_b()
d.show_c()
d.show_d()