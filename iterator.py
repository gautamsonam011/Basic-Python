# __iter__() and __next__()

mytuple = ("Apple", "Banana", "Cherry", "Grape")

myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

mystr = "India"
x = iter(mystr)
print(next(x))
print(next(x))
print(next(x))

# Looping through an iterator
for x in mytuple:
    print(x)

for x in mystr:
    print(x)    

# Create an Iterator 

# __iter__(), __next__() and __init__() 

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
obj = MyNumbers()
myiter = iter(obj)

print(next(myiter))
print(next(myiter))
print(next(myiter))

# StopIteration 

class MyNumbersAll:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
        
obj = MyNumbersAll()
itr = iter(obj)
for x in itr:
    print(x)        

# Function Polymorphism 

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")   

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")    

obj1 = Car("Tata", "Tigor")    
obj2 = Boat("Ibiza", "Touring 20")
obj3 = Plane("Boeing", "747")  

for x in (obj1, obj2, obj3):
    x.move()

# Inheritance class polymorphism 

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")

obj1 = Car("Tata", "Safari")
obj2 = Boat("Ibize", "456")
obj3 = Plane("Boeing", "587")

for x in (obj1, obj2, obj3):
    print(x.brand)
    x.move()