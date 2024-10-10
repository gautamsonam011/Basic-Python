# Creating a function 

def my_func():
    print("Hello World!")

my_func()  

# Arguments 

def my_add(x, y):
    print(x + y)

my_add(3, 6)

# Parameters or Arguments both are same 

# Number of arguments 

def my_func(fname, lname):
    print(fname + " " +lname)

my_func("Shiv", "Raj")    

# def customer(fname, lname):
#     print(fname + " " + lname)

# customer("Ankit")    customer() missing 1 required positional argument: 'lname'

# Arbitrary arguments, *args :- 

def my_func(*args):
    print("The younges child is " + args[2])

my_func("Sonam", "Gautam", "Raj")  

# Keyword Arguments 

def my_func(x, y, z):
    print("The youngest x is" + x)

my_func(x = 80, y = 32, z = 45)
    