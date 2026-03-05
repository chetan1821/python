import re
# email="chetan@gmail.com"
# pattern= r"^[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]{2,4}$"
# r=re.findall(pattern,email)
# print(r)


# password = input("Enter password: ")

# pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!])[A-Za-z\d@#$%^&+=!]{8,}$"

# if re.match(pattern, password):
#     print("Strong Password ✅")
# else:
#     print("Weak Password ❌")

import re

phone = "7228071014"

pattern = r"\d{10}"

if re.fullmatch(pattern, phone):
    print("Valid")
else:
    print("Not valid")