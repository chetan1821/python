# Write a Python program to update a value in a dictionary. 
dic={
    "name":"chetan",
    "age":20,
    "email":"cp123@gmail.com",
    "Eduction":"BCA",
    "Course":"python Backend",
    "Address":"surat"

}
# first method [normal method]
dic["age"]=21
print(dic)

# second method [using update method]
dic.update({"Eduction":"B.tech"})
print(dic)