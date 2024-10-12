# A lambda function is a small anonymous function 

# lambda arguments : expression 

x = lambda a : a +10
print(x(5))

x = lambda a, b: a*b
print(x(4,7))

x = lambda a, b, c: a+b+c
print(x(6, 7, 3))

# Why use lambda functions?

def myfunc(n):
    return lambda a:a*n

my = myfunc(4)

print(my(34))

def mySquare(n):
    return lambda a: a*n

x = mySquare(4)
y = mySquare(8)
print(x(10))
print(y(7))