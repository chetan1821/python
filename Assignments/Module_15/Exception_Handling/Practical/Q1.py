# Calculator with exception handling

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter operator (+, -, *, /): ")

    if op == "+":
        print("Result:", num1 + num2)
    elif op == "-":
        print("Result:", num1 - num2)
    elif op == "*":
        print("Result:", num1 * num2)
    elif op == "/":
        print("Result:", num1 / num2)   # may raise ZeroDivisionError
    else:
        print("Invalid operator")

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Please enter valid numbers")

except Exception as e:
    print("Unexpected Error:", e)