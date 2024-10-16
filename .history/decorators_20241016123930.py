# What is decorator ? 

# A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are typically applied to functions, and they play a crucial role in enhancing or modifying the behavior of functions.

# Assigning Functions to Variables:--------> 

def plus_one(number):
    return number +1

add_one = plus_one
print(add_one(5))

# Defining Functions inside other functions:-----> 

def add(number):
    def addFunc(number):
        return number + 2
    
    result = addFunc(number)
    return result

print(add(7))
