# def add(*a):
#     addtion=0
#     for i in a:
#         addtion += i
#     print(f"sum is {addtion}")

# add(10,20,30)
# add(45,98,63,82,60)
# add(1,2)

# 1️⃣ Print all values

# Write a function using *args that prints all values passed to it.

# def print_fun(*args):
#     for i in args:
#         print(i)

# print_fun(10,20,30)



# 2️⃣ Sum of numbers

# Write a function that accepts any number of integers using *args and prints their sum.
# def addtion(*args):
#     add =0
#     for i in args:
#         add += i
#     print(f"sum is {add}")

# addtion(45,65)
# addtion(79,4,5,9)


# 3️⃣ Count arguments

# Write a function that prints how many arguments were passed using *args.
# def count(*args):
#     print(len(args))
    
# count(10,20,30)
# count(7,8,9,5)

# 4️⃣ Find maximum number

# Write a function using *args to find the largest number.

def find_max(*args):
    if not args:
        print("No argument is function")
        return
    maxinum=args[0]
    for num in args:
        if num > maxinum:
            maxinum=num
    print("largest number is ",maxinum)

find_max(10, 20, 5, 40, 25)
find_max(3, 7, 2)
find_max(100)
find_max()

# 5️⃣ Multiply all numbers

# Write a function using *args that multiplies all numbers.

def mult_num(*args):
    if not args:
        print("No argument is function")
        return
    
    mul=1
    for i in args:
        mul *= i
    print("multiplication is : ",mul)

mult_num(10,20)
mult_num(4,5,6)
