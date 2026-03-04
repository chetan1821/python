
# List of strings
lines = [
    "Python is easy to learn.\n",
    "File handling is important.\n",
    "This file contains multiple strings.\n"
]

# Open file in write mode
file = open("example.txt", "w")

# Write multiple strings into the file
file.writelines(lines)

# Close the file
file.close()

print("Multiple strings written to the file successfully.")
