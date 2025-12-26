#datatype :
# Definition:
#A data type tells Python what kind of value a variable holds and 
#what operations can be performed on it.
#Python automatically decides the data type (dynamic typing).

# 1 . Numeric Data Types
#int
#float
#complex
a=10
b=15.6
c=4j+8
print(type(a))
print(type(b))
print(type(c))

# 2 . Sequence Data Types
#Used to store multiple values in order.
#string (str)
#list (Mutable) =>A list stores multiple values and can be changed.
#tuple (Immutable) =>Immutable = values cannot be modified
#range
print("******string*******")
string1 = "hello chetan"
print(type(string1))

print("******list*******")
l= [10,20,"chetan",12.45]
print(l)
print(type(l))

print("******tuple*******")
t=(10,23,56,98,"ffd",54.56)
print(t)
print(type(t))

print("******range*******")
r = range(1,5)
print(type(r))

# Mapping Data Type

#dictionary (dict)
#Definition:
#Stores data in key : value pairs.

d = {"name":"chetan","email":"abc@gmail.com"}
print(type(d))

#Set Data Type
#set
#A set stores unique values and removes duplicates.
s = {10,23,565,5898,"hj",56.22,23}
print(s)
print(type(s))


#Boolean Data Type
#Stores True or False values.
b = True
print(type(b))

#Type Conversion (Type Casting)
a = "10"
print(type(a))

k = int(a)
print(k)
print(type(k))






