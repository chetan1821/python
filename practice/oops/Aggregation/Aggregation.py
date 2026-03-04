# class Address:
#     def __init__(self,city,state):
#         self.city=city
#         self.state=state
    
# class Student:
#     def __init__(self,name,address):
#         self.name=name
#         self.address=address
#     def show(self):
#         print("Name : ",self.name)
#         print("Address : ",self.address.city)
#         print("Address : ",self.address.state)

# addr = Address("Surat","Gujarat")
# s=Student("chetan",addr)
# s.show()
        
class Book:
    def __init__(self,title):
        self.title=title


class Library:
    def __init__(self):
        self.book=[]
    def add_book(self,book):
        self.book.append(book)
    def show_books(self):
        for book in self.book:
            print(book.title)

b1 = Book("Java")
b2 = Book("Python")
b3=Book("cpp")
# print(b2.title)

l = Library()
l.add_book(b1)
l.add_book(b2)
l.add_book(b3)

l.show_books()


