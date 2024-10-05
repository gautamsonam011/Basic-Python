# Variables are containers for storing data values. 

# creating variables 

x = 30
y = "Lord Buddha"
print(x)
print(y)

z = 25
a = x+z
print(a)

# Casting 

b = str(6)
c = int(7)
d = float(8.9)
print(b)
# print(b+c)  can only concatenate str (not "int") to str

# Get the type type()

print(type(b))
print(type(z))

# Single or Double Quotes 

s = "Sonam"
g = 'sonam'
print(s)

# Python is a case sensitive programmimg language 
# age, Age and AGE, there are three different variables 

myvar = "Sonam"
my_var = "Sonam"
_my_var = "Sonam"
myVar = "Sonam"
MYVAR = "Sonam"
myvar2 = "Sonam"

print("myvar", myvar)
print("my_var", my_var)
print("_my_var", _my_var)
print("myVar", myVar)
print("MYVAR", MYVAR)
print("myvar2", myvar2)


# Multi words variable names 

# Camel Case:- Each word except the first, starts with a capital letter:

myVariableName = "Sonam"
print("This is a camel case:", myVariableName)

# Pascal Case:- Each word starts with a capital letter 

MyVariableName = "Sonam Gautam"
print("This is a pascal case:", MyVariableName)

# Snake Case :- Each word is separated by an underscore character: 

my_variable_name = "Sonam"

print("This is a snake case:", my_variable_name)

# Assign multiple values 

x, y, z = "Sonam", "Gautam", "Engineer"

print("First Name:", x)
print("Last Name:", y)
print("Profession:", z)

# One value to multiple variables 

x = y = z = "Radha"

print(x)
print(y)
print(z)

# Unpack a collection 

students = ["Riya", "Rohit", "Sonam", "Anjali"]

x, y, z = students

print(x)
print(y)
print(z)
