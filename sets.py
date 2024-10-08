# Python sets :- 

# Unordered 
# Unchangeable 
# Duplicates not allowed 

s = {"python", "java", "html", "css"}
print(s)

# type()
print(type(s))

# len()
print(len(s))

newSet = set(("Apple", "Banana", 34))
print(newSet)

# Access Set Items 

for i in s:
    print(i)

print("CSharp" in s)  

print("Apple" in newSet)

print(56 not in newSet)

# add() method 

s.add("orange")
print(s)

# Add Sets:- 

s1 = {46, -87, True, False, "Hello"}
s2 = {56, True, "Python", -23}

s1.update(s2)
print(s1)

s1 = {46, -87, True, False, "Hello"}
mylist = ["kiwi", "cherry"]

s1.update(mylist)
print(s1)

# remove() method

s3 = {"Org", "crg", "nvd"}
s3.remove("Org")
print(s3)

# discard() method

s3.discard("nvd")
print(s3)

# pop() method

s4 = {"apple", "banana", "cherry"}

x = s4.pop()
print(x)
print(s4)

# clear() method

s4.clear()
print(s4)

newset= {45, 78,21}

# del newset
# print(newset)   name 'newset' is not defined. Did you mean: 'newSet'?

# Loop Sets 

for i in newset:
    print(i)
    
# Join Sets 
# union()
# updated()
# intersection()
# difference()
# symmetric_difference()

set1 = {"a", "b", "c"}
set2 = {3, 5, 8}

set3 = set1.union(set2)
print(set3)

set4 = set1 | set2 
print(set4)

# Join multiple sets 

set5 = set1.union(set2, set3, set4)
print(set5)

myset = set1 | set2 | set4 
print(myset)

# Join a set and a tuple 
t = (54, 78,98)
z = set1.union(t)
print(z)

# update( ) 

set1.update(set2)
print(set1)

# intersection() 

s1 = {34, 67, 80, 43, 45}
s2 = {56, 89, 32, 45, 34}

s3 = s1.intersection(s2)
print(s3)

newS = s1 & s2
print(newS)

# intersection_update() 

s1.intersection_update(s2)
print(s1)

s1 = {34, 67, 80, 43, 45}
s2 = {56, 89, 32, 45, 34}
sD = s1.difference(s2)
print(sD)

setD = s1 - s2
print(setD)

# difference_update()

s1.difference_update(s2)
print(s1)

# symmetric_difference()

set3 = s1.symmetric_difference(s2)
print(set3)