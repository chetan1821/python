# Open the file in read mode
file = open("data.txt", "r")

# Read file content
content = file.read()
print("File Content:")
print(content)

file.close()
