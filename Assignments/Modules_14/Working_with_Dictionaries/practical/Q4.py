# Write a Python program to count how many times each character appears in a string. 
string = input("Enter a string: ")

char_count = {}

for ch in string:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1

print("Character count:")
print(char_count)
