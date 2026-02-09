# Write a Python program to merge two lists into one dictionary using a loop. 
keys = ['name', 'age', 'course']
values = ['Chetan', 21, 'BCA']

output = {}

for i in range(len(keys)):
    output[keys[i]] = values[i]

print("Merged Dictionary:", output)
