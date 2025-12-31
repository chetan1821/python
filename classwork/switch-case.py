choice =3
match choice:
    case 1:
        print("Gujarati")
    case 2:
        print("hindi")
    case 3:
        print("marathi")
    case _:
        print("Invalid input")


num_1 = int(input("Enter first value :"))
num_2 = int(input("Enter second value :"))
op=input("Enter operator : + , - , * , /")
choice=op
match choice:
    case '+' :
        print(num_1+num_2)
    case '-':
        print(num_1-num_2)
        
    case '*':
        print(num_1*num_2)
    case '/':
        print(num_1/num_2)
    case _:
        print("invalid input")

