age = int(input("Enter your age: "))
weight = float(input("Enter your weight (kg): "))

if age >= 18:
    if weight >= 50:
        print("You are eligible to donate blood.")
    else:
        print("You are NOT eligible because weight is less than 50 kg.")
else:
    print("You are NOT eligible because age is below 18.")
