class bankacc:
    def __init__(self, un):
        import random
        self.un = un
        self.number = random.randint(10,20)
        self.balance = 0
    def check(self):
        print(self.un)
        print("UNumber",self.number)
        print("Balance",self.balance)
    def deposit(self,a1):
        self.balance +=a1
        print(f"You paid {a1}")
    def withdraw(self,a2):
        if self.balance>= a2:
            self.balance -= a2
            print(f"You withdrawed {a2}")
        else:
            print("Insufficient funds")
        
Piotr = bankacc("Piotr")
Piotr.check()
Piotr.deposit(100)
Piotr.check()
Piotr.withdraw(150)
Piotr.check()