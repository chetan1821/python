# Method Overloading Example (using *args)

class Calculator:

    def add(self, *numbers):
        total = 0
        for i in numbers:
            total += i
        print("Sum:", total)


obj = Calculator()

obj.add(10)
obj.add(10, 20)
obj.add(10, 20, 30, 40)