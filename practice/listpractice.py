# l=[10,20,"chetan",55.5]
# print(l)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist)

# sec_method to create a list
# abc=list(("abc","def","ghi"))
# print(abc)
# print(len(abc))

# print(len(thislist))
# print(type(thislist))

#  Accessing list
# print(thislist[0])
# print(thislist[-1])
# print(thislist[1:3])
# print(thislist[4:6])
# print(thislist[::-1])
# print("mango" in thislist)

# change item in list
# thislist[0]="abc" # Add element of zero index => remove privous value add new value
# thislist[1:3]=[""] #remove the elements
# thislist.insert(2,"abcd")
# thislist.append("xyx")

# Extend list
# To append element from another list to current list
# this_1=[45,78,79]
# print(this_1)
# thislist.extend([10,20]) # normal list 
# thislist.extend(this_1) # differnt list use third variable
# print(thislist)
# print(this_1)



# Removes items
# thislist.remove("apple")
# thislist.pop() # remove the last element of list
# thislist.pop(2) # remove the spcific element using index
# thislist.clear() # return empty list
# del thislist # delete the list
# print(thislist)



# looping in list

# for i in thislist:
#     print(i)

# for i in range(len(thislist)):
#     print(thislist[i])

# i = 0
# while i < len(thislist):
#     print(thislist[i])
#     i+=1


# List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# without comprehension

# newlist=[]
# for i in thislist:
#     if 'a' in i:
#         newlist.append(i)

# print(newlist)

# with comprehension

# newlist = [i for i in thislist if 'b' in i]
# newlist = [i for i in thislist if i.endswith("e")]
# newlist = ["abc" for i in thislist]
# print(newlist)

# Sort method
# number_list = [10,89,2,8,45,45]
# number_list.sort()
# print(number_list)


# sorted method
number_list = [10,89,2,8,45,45]
# new_sorted=sorted(number_list)
# print(new_sorted)

# number_list.sort(reverse=True)
# number_list.reverse()
# print(number_list)

# copy of list
# mylist = thislist.copy()
# mylist = list(thislist)
# mylist = thislist[:]
# print(mylist)

# Join
# + oprator
list1 = [10,20,30,30,30]
list2= ["chetan","nikhil","jagdish"]
# list3=list1+list2
# print(list3)

# extend keyword
# list1.extend(list2)
# print(list1)

# count 
print(list1.count(30))

# max
print(max(list1))
print(min(list1))













