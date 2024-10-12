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