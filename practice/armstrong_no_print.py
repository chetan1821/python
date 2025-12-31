for num in range(100, 1001):
    temp = num
    arm = 0

    while temp != 0:
        rem = temp % 10
        arm = arm + (rem ** 3)
        temp = temp // 10

    if arm == num:
        print("Armstrong number:", num)
