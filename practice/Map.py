# subjects=["python","php","java","android"]
# new_map=map(lambda a: len(a),subjects)
# print(list(new_map))

# l1 = [10,25,7,3,2]
# b = []

# def odd_fun(a):
#     if a % 2 != 0:
#         return a

# for i in range(len(l1)):
#     k = odd_fun(l1[i])
#     if k is not None:
#         b.append(k)

# print(b)

subject = ["python","java","php","android"]

def demo_fun(a):
    if 'p' in subject:
        print("Contains p ",subject)
        return a

for i in range(len(subject)):
    demo_fun(subject[i])             

