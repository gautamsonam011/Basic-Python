# Abstract 

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("Car started....")

c = Car()
c.start()   

# Encapsulation 




# Let's Practice 

# Create account class with 2 attributes - balance & account no. 
# Create methods for debit, credit & printing the balance. 

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs", amount, "was debited")
        print("Total balance =", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs", amount, "was credited")
        print("Total balance=", self.get_balance()) 

    def get_balance(self):
        return self.balance       

acc1 = Account(5000, 1100008373)
print(acc1.balance)
print(acc1.account) 

acc1.debit(1000)

        