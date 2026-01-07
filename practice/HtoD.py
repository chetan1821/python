hex_num = "9B"
decimal = 0
power = 0

a = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

while hex_num != "":
    rem = hex_num[-1]            # take last character
    value = a.index(rem)         # get decimal value
    decimal = decimal + value * (16 ** power)
    power += 1
    hex_num = hex_num[:-1]       # remove last character

print(decimal)



# octal->decimal
# heax->decimal
