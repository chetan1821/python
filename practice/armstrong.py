num = int (input("Enter number :"))
arm = 0
temp = num

while num >0:
    rem=num%10
    # print(rem)
    arm=(rem*rem*rem)+arm
    # print(arm)
    num=num//10
    # print(num)

if temp == arm:
    print("armstrong number")
else:
    print("its not armstrong number")
