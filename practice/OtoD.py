num=777
octal=0
power = 0
while num !=0:
    rem=num%10
    octal=octal+rem*(8 ** power)

    power +=1
    num=num//10
    
print(octal)


# octal->decimal
# heax->decimal
