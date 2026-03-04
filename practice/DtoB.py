num=155
n=0
m=1

while num != 0:
    rem=num%2
    n = (rem*m)+n
    num = num//2
    m*=10

print(n)
