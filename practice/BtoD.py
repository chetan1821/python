num=10010000
decimal=0
power = 0
while num !=0:
    rem=num%10
    decimal=decimal+rem*(2 ** power)

    power +=1
    num=num//10
    
print(decimal)


# octal->decimal
# heax->decimal
