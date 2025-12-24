# print function in python

# string writing format
print("hello chetan")
print('hello python')
print("""
hello this is 
doc string 
this help
""")
# printing quotes inside string 
print("hello\"this\" is me")

a=10
print(a)

# name="chetan"
# print(name)

# print multiple values
x=20
y=10
print(x,y)

# using sep parameter
# sep decides how values are separated.
print("chetan","nikhil","jagdish",sep=" | ")
print("22","12","2025",sep="-")

# using end parameter
print("this is ",end="")
print("chetan")

name="chetan"
email="chetan123@gmail.com"
print("hello my name is {0} and my email id is {1}".format(name,email))
print(f"hello my name is {name} and my email id is {email}")

#printing expresion
print(10+2)