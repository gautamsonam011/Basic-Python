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