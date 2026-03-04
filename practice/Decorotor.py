def decorotor_fun(origal_fun):
    def wrapper():
        print("Before function")
        origal_fun()
        print("After function")
    return wrapper
def display():
    print("hello chetan")

new_dec=decorotor_fun(display)
new_dec()

