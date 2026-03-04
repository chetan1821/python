from abc import ABC,abstractclassmethod

class Account(ABC):
    balance =0
    @abstractclassmethod
    def deposite(self,amount):
        pass
    @abstractclassmethod
    def withdrow(self,amount):
        pass

    def get_balance(self):
        print(f"Current Balance is {self.balance}")

class SavingAccount(Account):
    def deposite(self, amount):
        self.balance += amount
    def withdrow(self, amount):
        if amount > self.balance:
            print("Insufisent balance")
        else:
            self.balance -= amount

class Loan(Account):
    def withdrow(self, amount):
        self.balance += amount
    def deposite(self, amount):
        if amount > self.balance:
            extra = amount - self.balance
            print(f"Return extra amount: {extra}")
            self.balance = 0
        else:
            self.balance -= amount



saving=SavingAccount()
# saving.get_balance()
# saving.deposite(5000)
# saving.get_balance()
# saving.withdrow(1000)
# saving.get_balance()

l=Loan()
l.get_balance()
l.withdrow(1000)
l.deposite(1100)
l.get_balance()
# saving.get_balance()




