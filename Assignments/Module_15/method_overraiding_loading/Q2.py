# Method Overriding Example

class Animal:

    def sound(self):
        print("Animal makes sound")


class Dog(Animal):

    def sound(self):   # Overriding parent method
        print("Dog barks")


class Cat(Animal):

    def sound(self):   # Overriding parent method
        print("Cat meows")


# Object creation
a = Animal()
d = Dog()
c = Cat()

a.sound()
d.sound()
c.sound()