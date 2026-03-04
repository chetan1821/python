# line=5
# star = line
# space=0
# for i in range(line):
#     for k in range(line-i-1):
#         print(" ",end="")
#     for j in range((i*2)-1):
#         print("*",end="")


#     print()
#     star -=1
#     space=1



# row = 5
# for i in range(row):
#     for k in range(i):
#         print(" ",end="")
#     for j in range(row-i):
#         print("* ",end="")
#     print()

lines = 5

# upper part
stars = 1
space = (lines - 1) * 2

for i in range(lines):
    for j in range(stars):
        print("*", end="")
    for k in range(space):
        print(" ", end="")
    for j in range(stars):
        print("*", end="")
    print()

    stars += 1
    space -= 2


# lower part
stars = lines - 1
space = 2

for i in range(lines - 1):
    for j in range(stars):
        print("*", end="")
    for k in range(space):
        print(" ", end="")
    for j in range(stars):
        print("*", end="")
    print()

    stars -= 1
    space += 2
