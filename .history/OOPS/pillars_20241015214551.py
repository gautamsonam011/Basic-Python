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

from abc import ABC, abstractmethod
class Baseclass(ABC):
    @abstractmethod
    def my_method(self):
        pass

class Cars(ABC): 
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.engine_started = True

    def startEngine(self):
        if not self.engine_started:
            print(f"Starting the {self.color}'s engine")
            self.engine_started = True
        else:
            print("Engine is already runing.") 
obj = Cars("Tata", "White")                     
print(obj.startEngine())

class CarA(ABC):
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year

    @abstractmethod
    def car_details(self):
        pass

    def accelerate(self):
        print("Speed up...")

    def break_applied(self):
        print("Car stopped")

class Hatchback(CarA):
    def car_details(self):
        print("Brand:", self.brand)
        print("Color:", self.color)
        print("Year:", self.year)

    def sunroof(self):
        print("Not having this features")

class Suv(CarA):
    def car_details(self):
        print("Brand:", self.brand)
        print("Color:", self.color)
        print("Year:", self.year)

    def sunroof(self):
        print("Available")   

obj = Hatchback("Maruti", "Black", "2024")
obj.car_details()
obj.accelerate()
obj.sunroof() 


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
acc1.credit(4000)

# Protected :- 

class Parent:
    def __init__(self):
        self._a = 3

class Child(Parent):
    def __init__(self):
        # Calling constructor of parent class 
        Parent.__init__(self)
        print("Calling protected member of parent class", self._a)

        self._a = 5
        print("Calling modified protect member outside class", self._a)


obj = Child()
obj1 = Parent()
print("Accessing protected member of parent class:", obj1)
print("Accessing protected member of child class:", obj)

# Private :- 

class Base:
    def __init__(self):
        self.a = "MYCourse"
        self.__c = "Mycourse"

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling private member of base class")
        print(self.__c)   

obj = Base()
print(obj.a)  
print(obj.__c)           

