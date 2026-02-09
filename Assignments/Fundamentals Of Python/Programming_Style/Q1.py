# This program calculates the average of three numbers
# It demonstrates proper indentation, comments, and variables (PEP 8)

def calculate_average(num1, num2, num3):
    
    total = num1 + num2 + num3
    average = total / 3
    return average


# Input values
number_one = 10
number_two = 20
number_three = 30

# Function call
result = calculate_average(number_one, number_two, number_three)

# Output result
print("The average is:", result)