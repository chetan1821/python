number = int(input("Enter any number : "))
flag = 0
for i in range(2,number):
   if number%i==0:
        flag =1
        break
   
if flag==0:
    print("prime")
else:
    print("Not prime")