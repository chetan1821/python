# Hybrid Inheritance
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

obj = D()
obj.show_a()
obj.show_b()
obj.show_c()
obj.show_d()