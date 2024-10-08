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

# Extend List 

x = ["Sona", "Shiv", "Ram"]

list.extend(x)
print(list)

# Remove list items :- remove()

list = ["apple", "banana", "cherry", "orange"]
print(list)
list.remove("banana")
print(list)

# Remove specified index 

# pop()

list.pop(0)
print(list)

list.pop()
print(list)

# The del keyword also removes the specified index 

del list[0]
print(list)

# Clear the list 
# clear()
list = [45,78,22]
list.clear()
print(list)

# ========= Loop Lists =======> 

# Loop through a list:- 

list = ["apple", "banana", "cherry"]
for x in list:
    print(x)

# Loop through the index numbers 

# range(), and len()

for i in range(len(list)):
    print(list[i])

# Using a while loop 

i = 0
while i < len(list):
    print("Using a while loop:", list[i])

    i = i+1    

# Looping using list comprehension:- 

[print(i) for i in list]    

students = ["Sonam", "Ram", "Savita", "Abhi"]

newlist = []

for i in students:
    if "S" in i:
        newlist.append(i)
        
print(newlist) 

newlist = [i for i in students if "R" in i]
print(newlist)

newlist = [i for i in students if i != "Abhi"]
print(newlist)

x = [i for i in range(10)]
print(x)

x = [i for i in range(0, 11) if i < 5]
print(x)

x = [i.upper() for i in students ]
print(x)

x = ['hello' for i in students]
print(x)

x = [i if i != "Ram" else "Abhi" for i in students]
print(x)

# Sort List Alplanumerically 

# sort()

list = ["python", "java", "html", "css"]
list.sort()
print(list)

x = [46,87,32,45,75]
x.sort()
print(x)

# Sort Descending 
# reverse = True 

list.sort(reverse = True)
print(list)

x.sort(reverse = True)
print(x)

# Customize sort function 

def func(n):
    return abs(n - 50)

list = [46, 78, 321, 46, 78]
list.sort(key = func)
print(list)

# Case Insensitive Sort 

# sort()

list = ["banana", "Kiwi", "cherry", "Orange"]
list.sort()
print(list)

list.sort(key = str.lower)
print(list)

list.reverse()
print(list)

# ========= Copy Lists ==========> 

# copy() method 

newlist = list.copy()
print(newlist)

# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)

# Use the slice operator 

x = ["python", "jave", 355, -65]
newlist = x[:]
print(newlist)

print(x[1:3])
print(x[:1])

# Join Lists 

list1 = ["Python", "Hello", "Java", 465, False]
list2 = [324, 56, 67.44, "Java"]

list3 = list1+list2
print(list3)

# append()

for x in list2:
    list1.append(x)
print(list1)    