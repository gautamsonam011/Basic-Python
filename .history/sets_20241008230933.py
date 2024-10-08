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