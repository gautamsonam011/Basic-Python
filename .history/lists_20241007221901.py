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

# Range of indexes (positive)

print(l[3:6])

# Range of indexes (negative)
print(l[-6:-3])

# Check if item exists 

if "Python" in l:
    print("Yes!")
    
# Change Item Value 

# replace 

list = ["apple", "banana", "cherry"]

list[1] = "orange"
print(list)

# change in range 

list[1:3] = ["Hello", "Python"]
print(list)

# Insert Items in list insert()

list.insert(3,-7) #(index, item)
print(list)

# Append( )

list.append("orange")
print(list)