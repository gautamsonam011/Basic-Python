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
    print("The youngest x is" + str(x))

my_func(x = 80, y = 32, z = 45)

# Arbitrary Keyword Arguments 

def my_func(**kid):
    print("His last name is" + kid["lname"])

my_func(fname = "Sonam", lname = "Gautam")    


def my_function(country = "Bharat"):
  print("I am from " + country)

# my_function("India")
my_function()

# Passing a List as an Argument 

def my_page(food):
    for x in food:
        print(x)

fruits = ["Apple", "Banana", "Orange"]

my_page(fruits)

# Return values 

def my_return_values(x):
    return 5 * x

print(my_return_values(56))

# The pass Statement 

def mypass_func():
    pass

# Positional only arguments 

def my_positional(x, /):
    print(x)

my_positional(54)

def my_func(x):
    print(x)

my_func(x = 45)

# def my_function(x, /):
#     print(x)

# my_function(x = 5)    my_function() got some positional-only arguments passed as keyword arguments: 'x

# Keyword only arguments 

def my_keyword(*, y):
    print(y)

my_keyword(y = 34)    