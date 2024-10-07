mylist = ["python", "java", "django", "fastapi"]

print(mylist)
print(type(mylist))

print(len(mylist))

x = [3,5,7,8,9]
print(type(x))
print(len(x))

y = [True, False]
print(y)
print(len(y))
print(type(y))

l = [54, 78, "Python", "Hello", True, False, -47, 85.4]
print(type(l))
print(l)
print(len(l))

# The list() constructor 

list = list(("apple", "Hello", 54, True))
print(list)

# Access List items 

l = [54, 78, "Python", "Hello", True, False, -47, 85.4]

# By positive index 

print(l[5])

# By negative index 

print(l[-5])

# Range of indexes 

print(l[3:6])