# Handling multiple exceptions

try:
    file = open("data.txt", "r")   # may raise FileNotFoundError
    num = int(input("Enter number: "))
    result = 100 / num             # may raise ZeroDivisionError

    print("Result:", result)

except FileNotFoundError:
    print("Error: File not found")

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Invalid input")

finally:
    print("Program finished")