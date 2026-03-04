class student:
    sid=1
    sname = "chetan"
    email = "cp72@gmail.com"

    def display(self):
        print(self.sid,self.sname,self.email)

s1 = student()
# s1.sname="jagdish"
s1.display()
s2=student()
s2.sid = 2
s2.sname = "jagdish"
s2.email="jp789@gmail.com"
s2.display()
