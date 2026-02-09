# Practical Example 6: Write a Python program to check if a number is prime using if_else.

num = int(input("Enter a number : "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not prime")
            break
    else:
        print(f"{num} is prime")
else:
    print(f"{num} is not prime")
