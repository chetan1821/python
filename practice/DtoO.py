number = 155
# n = ""
n = 0
m = 1
while number!=0:
    rem = number%8
    # n = str(rem)+n
    n = (rem*m)+n
    number = number//8
    m*=10

print(n)

