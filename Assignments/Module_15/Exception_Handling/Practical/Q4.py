# Custom exception example

class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter age: "))

    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")

    print("You are eligible")

except InvalidAgeError as e:
    print("Custom Exception:", e)

except ValueError:
    print("Invalid input")