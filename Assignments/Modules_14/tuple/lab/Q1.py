# Write a Python program to create a tuple with multiple data types.
t=(10,12.35,"chetan",True,False,5j+4,[1,2,3],{25,65},{"name":"chetan","age":20})
print(t)

for i in t:
    print(i,"=>",type(i))