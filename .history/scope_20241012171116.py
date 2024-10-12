# Local Scope :- 

def myfunc():
    x = 400
    print(x)     #scope 

myfunc()  

# Function Inside Function 

def myFunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myFunc()   

# Global Scope 

x = 56

def myfunc():
    print(x)

myfunc()

print(x)

# Naming Variables 

y = 500

def myfunc():
    y = 576
    print(y)

myfunc()
print(y)  

# Global Keyword 

def myfunc():
    global x
    x = 589

myfunc()
print(x)    

z = 456
def myNumber():
    global z
    z = 3000

myfunc()

print(z)

# Non Local Keyword

def func1():
    s = "Sonam"
    def func2():
        nonlocal s 
        s = "Hello!"
    func2()
    return s

print(func1())   
# print(s)        