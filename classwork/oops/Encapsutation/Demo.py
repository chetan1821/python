class Student:

    __id=10 # private member in python 
    

    def set(self,id):#change the value in __id 
        self.__id=id

    def get(self):
        print(self.__id)

s=Student()
s.set(20)
s.get()