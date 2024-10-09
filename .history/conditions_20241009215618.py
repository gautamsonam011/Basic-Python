# Python Conditions and If statements:- 

# Python supports the usual logical conditions fron mathematics: 

a = 45
b = 67
if b > a:
    print("B is greater than A")

# Indentation 

x = 43
y = 32
# if x > y:
# print("X is greater than Y")    expected an indented block after 'if' statement

# Elif and else

if x > y:
    print("x is greater than y")

elif x == y:
    print("Equal")
else:
    print("y is greater than x")        

# Short hand if 
a = 43
b = 7
if a > b: print("a is greater than b")    

# Short hand if ... else 

a = 65
b = 300

print("A") if a > b else print("B")

a = 43
b = 43

print("A") if (a > b) else print("Equal") if a == b else print("B")

# And 

x = 6
y = 3
z = 8

if (x > y) and (z > x):
    print("Both conditions are True")

# OR 

if (x > y) or (x > z):
    print("True")    