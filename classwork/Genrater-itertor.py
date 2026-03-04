# l=[10,20,30,40]
# k= iter(l)
# print(next(k))
# print(next(k))
# print(next(k))
# print("hello")
# print(next(k))


# yield &return

# def test():
#     yield "hello"
#     yield "chetan"

# k=test()
# print(next(k))
# print(next(k))

def demo(a):
    for i in range(a):
        yield i*i

sq=demo(5)
print(next(sq))