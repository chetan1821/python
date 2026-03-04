# class Calc:
#     def add(self,*a):
#         sum=0
#         for i in a:
#             sum+=i
#         print(sum)

# c=Calc()
# c.add(10,20)
# c.add(20,30,60)


class Over:
    def add(self,a,b):
        print(f"Sum :{a+b}")
    def add(self,a,b,c):
        print(f"sum : {a+b+c}")
    
o=Over()
o.add(10,20,20)
o.add(30,20,60)