class demo:
    name = "chetan" # class property
    age = 20

    def __init__(self):
        self.course = "BCA" # do not access in classmethod only access instance
    def display(self):
        print(self.name,self.course,self.age)

    @classmethod
    def test(cls):
        print(cls.age,cls.name)

    
        


d = demo()
d.display()
d.test()

