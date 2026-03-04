# A decorator is a function that modifies another function’s behavior without changing its code.

# 👉 Decorators use:

# Functions as arguments

# Nested functions

# @decorator_name syntax



# def greet(fx):
#     def mfx():
#         print("Good morning..")
#         fx()
#         print("thanks for using..")
#     return mfx

# @greet
# def hello():
#     print("hello")

# hello()

def login_required(func):
    def wrapper(user):
        if user == "admin":
            return func(user)
        else:
            print("Access denied")
    return wrapper

@login_required
def dashboard(user):
    print("Welcome to dashboard")

dashboard("admin")
dashboard("guest")
 
