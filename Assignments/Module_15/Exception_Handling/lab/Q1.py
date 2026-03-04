# Write a Python program to handle exceptions in a simple calculator (division by zero, invalid 
# input)

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2

    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

else:
    print("Calculation completed successfully.")

finally:
    print("Program execution finished.")

