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