#map()

# nums = [1,2,3,4,5]
# new_num = list(map(lambda x : x+2 , nums))
# print(new_num)

# def squre(a):
#     return a*a

# num = [10,20,30]
# print(list(map(squre,num)))
# new_list = list(map(lambda x : x*x,num))
# print(new_list)

# convert string to interger
# list_1 = ["10","20","30"]
# print(list_1)
# res=list(map(int,list_1))
# print(res)

# map() with Multiple Iterables

# l1=[1,2,3,4]
# l2=[4,3,2,1]
# l3=list(map(lambda x,y : x+y ,l1,l2))
# print(l3)

# QA Set

# Double all values:
# l=[2,4,6,8]
# new_list=list(map(lambda x : x*2,l))
# print(new_list)

# Convert strings to int:
# l=["5","10","50"]
# new_list = list(map(int,l))
# print(new_list)

# Find square of each number:
# l=[1,2,3,4]
# new_list = list(map(lambda x : x*x,l))
# print(new_list)

# Add two lists:
# a=[1,2,3]
# b=[4,5,6]
# new_list = list(map(lambda x,y : x+y,a,b))
# print(new_list)

# Convert names to uppercase:
# names=["chetan","rahul","amit"]
# new_list=map(lambda x : x.upper(),names)
# print(list(new_list))


# Extract length of each word:

# words=["python","java","sql"]
# new_words = list(map(lambda x : len(x),words))
# print(new_words)


# Multiply each element by index:

l=[10,20,30]
result = list(map(lambda x ,i : x*i,l,range(len(l))))
print(result)







