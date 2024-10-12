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