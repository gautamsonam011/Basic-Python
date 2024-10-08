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