try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2
    print("Result:", result)

except ValueError:
    print("Error: Invalid input! Please enter integers only.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except Exception as e:
    print("Unexpected error occurred:", e)

else:
    print("Program executed successfully.")

finally:
    print("End of program.")
