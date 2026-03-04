# filter()
# list1=[1,2,3,4,5,6,7]
# def is_even(n):
#     return n % 2 == 0
    
# result = list(filter(is_even,list1))
# print(result)

# with lambda
# result = list(filter(lambda x:x%2==0,list1))
# print(result)

# names=["chetan","om","jagdish","jay"]
# result= list(filter(lambda x: len(x)<3,names))
# print(result)

# filter none
# data = [1,2,"","chetan",None,"patil",32.2]
# result = list(filter(None,data))
# print(result)

# nums = [1,2,3,4,5,6]
# result = list(map(lambda x:x*x,filter(lambda x : x % 2==0,nums)))
# print(result)

# **************************
# Practice Questions
# **************************
# data=[10,15,20,25,30]
# print(list(filter(lambda x : x%2==0,data)))

# data = [10,60,45,80,25]
# print(list(filter(lambda x : x>50,data)))

# names=["ram","shyam","om","chetan"]
# print(list(filter(lambda x : len(x)>4,names)))

# nums =[-10,5,-3,8,0]
# print(list(filter(lambda x : x>0,nums)))

# vowels=['a','b','e','f','i','o']
# print(list(filter(lambda x : x in ["a","e","i","o","u"],vowels)))

# data = [1,2,3,4,5]
# result = filter(lambda x : x % 2 !=0,map(lambda x : x*2,data))

# print(list(result))

# empty_str=["hi","","hello",None,""]
# print(list(filter(None,empty_str)))

# marks = [45,67,82,50,90]
# print(list(filter(lambda x : x > 60,marks)))

# palindrome = ["madam","python","level","java"]
# result = filter(lambda x : x[::-1]==x,palindrome)
# print(list(result))


marks = {"ram": 45, "shyam": 78, "amit": 60, "rahul": 30}

result = dict(filter(lambda item: item[1] > 50, marks.items()))
print(result)










