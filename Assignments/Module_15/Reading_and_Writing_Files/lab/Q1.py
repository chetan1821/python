# Write a Python program to read the contents of a file and print them on the console.
# file = open("data.txt","w")
# file.write("hello python Devloper..\n")
# file.write("HELLO MY NAME IS CHETAN..")
# file.close()

file = open("data.txt","r")
print(file.read())
file.close()
