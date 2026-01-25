# A set is a collection which is unordered, unchangeable*, and unindexed.
# Do not allow DUplicate values

# Normal Set
# myset={"Apple","Banana","cherry","Apple"}
# print(myset)
# print(len(myset))

# # Set constroctor
# thisset=set(("hello","chetan","patil"))
# print(thisset)

#Access set items
# for _ in thisset:
#     print(_)

# print("hello" in thisset) #=>True
# print("banana" not in thisset) #=>True

# Add items in set

# 1.Add() => To add one item to a set use the add() method.
# thisset.add("orange")
# print(thisset)

# 2.update()=> To add items from another set into the current set, use the update() method.
# set_1={"laptop","Mouse","CPU","speker"}
# set_2={55000,1200,8500,3000}
# set_3={"Lenovo","Acer","hp","Dell"}
# set_1.update(set_2,set_3)
# print(set_1)

# Remove items

# 1.remove(): To remove an item in a set, use the remove(), or the discard() method.
# If the item to remove does not exist, remove() will raise an error.
# set_1={"laptop","Mouse","CPU","speker"}
# set_1.remove("CPU")
# print(set_1)

# Discard(): Remove "CPU" by using the discard() method:
#  If the item to remove does not exist, discard() will NOT raise an error.
# set_1={"laptop","Mouse","CPU","speker"}
# set_1.discard("banana")
# print(set_1)

# pop => random value remove
# set_1={"laptop","Mouse","CPU","speker"}
# set_1.pop()
# print(set_1)

# clear() 
# set_1={"laptop","Mouse","CPU","speker"}
# set_1.clear()
# print(set_1)

# del()
# set_1={"laptop","Mouse","CPU","speker"}
# del set_1
# print(set_1)


# join set 

# 1. union => join set => |
# set_1={"laptop","Mouse","CPU","speker"}
# set_2={55000,1200,8500,3000}
# set_3={"Lenovo","Acer","hp","Dell"}
# new_set=set_1.union(set_2)
# new_set2=set_1 | set_2 | set_3
# print(new_set2)
# print(new_set)

# 2.join tuple and set
# s={"a","b","c","d",(10,20)}
# print(list_1.append[3].add("patil"))
# t=[10,20,30,40]
# st=s.union(t)
# print(st)

# 3. intersection => & 
# The intersection() method will return a new set, that only contains the items that are present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

# set3 = set1.intersection(set2)
# set3= set1&set2
# print(set3)

# 3.1 The intersection_update() 
# method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.













