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

acc1 = Account(5000, 1100008373)
print(acc1.balance)
print(acc1.account)        
        