# Classes/Objects 

# Create a class 
class myclass:
    x = 59

#  Create a object 
p1 = myclass()
print(p1.x)  

# The __init__() Function 

class Person:
    def __init__(self, name, age, designation):
        self.name = name
        self.age = age
        self.designation = designation

obj = Person("Sonam", 26, "Software Developer") 
print(obj.name)
print(obj.age)
print(obj.designation)       

# The __str__() Function 

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

obj = Student("Jiya", 20)
print(obj)

class Parents:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

obj = Parents("Ankit", 28)
print(obj)        

# Object Methods 

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

obj = Student("Golu", 34)
obj.myfunc()  

# The self Parameter 

class Employee:
    def __init__(my, name, age):
        my.name = name
        my.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)

obj = Employee("Ridhi", 32)
obj.myfunc()   

# Modify Object Properties 

obj.age = 56
print(obj.age)

# Delete object Properties 

# del 

del obj.age

print(obj.age)