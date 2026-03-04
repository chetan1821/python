# row = 5
# for j in range(row):
#     for i in range(row):
#         print("*",end="")
#     print()


# for i in range(5):
#     print("*"*5)

# *****
# *****
# *****
# *****
# *****

# row=5
# for i in range(row):
#     for j in range(i+1):
#         print("*",end="")
#     print()

# for i in range(row):
#     print("*"*(i+1))

# *
# **
# ***
# ****
# *****

# row = 5
# for i in range(row):
#     for j in range(row-i):
#         print("*",end="")
#     print()

# print("------------")

# for i in range(row):
#     print("*"*(row-i))

# *****
# ****
# ***
# **
# *


# row = 5
# for i in range(row):
#     for space in range(row-(i+1)):
#         print(" ",end="")
#     for j in range(i+1):
#         print("*",end="")
#     print()

# print("--------------")
# for i in range(row):
#     print(" "*(row-(i+1)),"*"*(i+1))

#     *
#    **
#   ***
#  ****
# *****

# row = 5
# for i in range(row):
#     for k in range(i,row):
#         print(" ",end="")
#     for j in range(i):
#         print("* ",end="")
#     print()
# for i in range(row):
#     for x in range(i):
#         print(" ",end="")
#     for y in range(row-i):
#         print("* ",end="")
    

#     print()

    

#      * 
#     * *
#    * * *
#   * * * *
#  * * * * *

# row = 5
# for i in range(row):
#     for k in range(i):
#         print(" ",end="")
#     for j in range(row-i):
#         print("* ",end="")
#     print()


row = 5
for i in range(row):
    for k in range(i,row):
        print(" ",end="")
    for j in range(i):
        if j == 0 or j == i - 1:
            print("* ",end="")
        else:
            print("  ", end="")
    print()
for i in range(row):
    for x in range(i):
        print(" ",end="")
    for y in range(row-i):
        if y == 0 or y== row-i-1:
            print("* ",end="")
        else:
            print("  ", end="")
    
    print()





