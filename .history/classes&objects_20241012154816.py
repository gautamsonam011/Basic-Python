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