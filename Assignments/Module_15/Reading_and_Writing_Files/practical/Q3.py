# Open file in read mode
file = open("data.txt", "r")

# Read some data
file.read(10)

# Get current cursor position
position = file.tell()
print("Current file cursor position:", position)


file.close()
