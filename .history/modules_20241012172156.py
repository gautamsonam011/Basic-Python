# A file containing a set of functions you want to include in your application.

# Create a module 

# def greeting(name):
#     print("Hello! " + name)

# Use a Module 

import modulefunctions

modulefunctions.greeting("Aniket.")

# Variables in Module 

a = modulefunctions.employee["age"]
print(a)

b = modulefunctions.employee["country"]
print(b)

# Naming a Module 

# Re-naming a Module 
import modulefunctions as mf

c = mf.employee["name"]
print(c)