# Write a Python program that uses a custom iterator to iterate over a list of integers. 
# Custom iterator using a generator function (without class)

def custom_iterator(numbers):
    for num in numbers:
        yield num


# List of integers
num_list = [10, 20, 30, 40, 50]

# Using the custom iterator
for value in custom_iterator(num_list):
    print(value)
