count=0
for number in range(1, 101):
    
    if number <= 1:
        continue   
    flag = 0
    for i in range(2, number):

        if number % i == 0:
            flag = 1
            
            break
            

    if flag == 0:
        count += number
        print(number, "is prime")
    else:
        pass
        # print(number, "is not prime")
print("sum = ",count)
