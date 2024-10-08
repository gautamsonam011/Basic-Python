# Tuple 

mytuple = ("python", "java", True, 36, -67)

print(mytuple)

# Ordered
# Unchangeable 
# Allow duplicates 

t = ("python", "css", True, False, True, 300, -2)
print(t)

# Tuple Length len()

print(len(t))
print(type(t))

# The tuple() constructor 

newt = tuple((367, 467,22))
print(newt)

list = [34, 67, 42, 84, 49]
t = tuple(list)
print(t)

# Access Tuple items 
# By positive index 

print(t[3])

# By negative index 

print(t[-3])

# Range of index 

print(t[2:4])

print(t[-4:-1])

print(t[:2])
print(t[3:])

# Check if item exists 

if 42 in t:
    print("Yes!")

# Update Tuple 

# Change Tuple values 

# Unchangeable and immutable

# x2 = ("apple", "banana", "cherry")

# y = list(x2)

# y[1] = "kiwi"

# x3 = tuple(y)
# print(x3)

# y.append("orange")
# thistuple = tuple(y)

# Unpacking a tuple 

s = ("lsd", "laravel", "javascript", "react")

(a , b, c, d) = s
print(a)
print(b)
print(c)
print(d)

# Using Asterisk * 

(a,b, *c) = s
print(a)
print(b)
print(c)

(a, *b, d) = s
print(a)
print(b)
print(d)

# Loop through a tuple 
for i in s:
    print(i)

# Loop through the index number 

for i in range(len(s)):
    print(s[i])    
    
# Using a while loop 

i = 0

while i < len(s):
    print(s[i])
    i = i+1
    
# Join Two Tuples 

tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# multiply tuples 

mytuple = tuple1 * 5
print(mytuple)

tup = tuple2 * 2
print(tup)

