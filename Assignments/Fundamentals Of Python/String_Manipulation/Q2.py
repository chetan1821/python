st = "sun rise In East"

# String len count the length of string
print(len(st))

#lower convert uper to lower
print(st.lower())

# case fold => 
print(st.casefold())

#title => first char is upper in word
print(st.title())

#uper => lower to upper
print(st.upper())

#strip =>
print(st.strip())

#Replace old char => new char
# print(st.replace("s","k",2))

# find char or word => find
print(st.find('r'))

# startwith => check to the string is exact start with char or word
# returen tru or false
print(st.startswith('s'))

# endwith =>chaeck string endwith exact char or word
# returen tru or false
print(st.endswith('a'))

#split the string in space 
print(st.split(" ",2))

#join 
# print(st.join("abc"))

# isalph check string have only alphabest
print("abcs".isalpha())

#isdigit check string have only number
print("123".isdigit())

# its have both things number and words
print("123Abc".isalnum())

#z.fill 
print("chetan".zfill(10))

#string start in center
print("chetan".center(12,'*'))


