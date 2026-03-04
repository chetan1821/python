# dic_1={
#     "name":"chetan",
#     "Email":"cp123@gmail.com",
#     "contact":"789456123",

#     "list_1":["hello","hey"],
#     "tuple_1":(10,20,30),
#     "set_1":{50,60,70}

# }
# print(dic_1)
# print(len(dic_1))
# print(dic_1["contact"])
# print(dic_1["list_1"][0])
# print(dic_1.get("Email"))


# print(dic_1.keys())
# print(dic_1.values())
# print(dic_1.items())

# Access Elements By loops
# for i in dic_1:
#     print(i)

# for i,j in dic_1.items():
#     print(i,j)

# person = {
#     "name":"Chetan",
#     "email":"chetan@gmial.com"
# }

def student(**a):
    print(a)

student(name="abc",email="abc@gmail.com",ph=722806105)



