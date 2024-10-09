# Dictionary:-
# Dictionaries are used to store data values in key:value pairs.

dict = {
    "name": "Ram",
    "age": 45,
    "course": "Python"
}

print(dict)
print(dict["name"])
print(type(dict))

# Ordered or Unordered 
# changeable
# Duplicates not allowed 

# Dictionary length 

print(len(dict))

# The dict() constructor 

# dict()

# dict_data = dict(name = "Sona", age = "36", country = "Indian")
# print(dict_data)

# Accessing Items 

x = dict["age"]
print(x)

# get()

x = dict.get("name")
print(x)

# Get Keys 

# keys()

x = dict.keys()
print(x)

dict["country"] = "India"
print(dict)

# values()

x = dict.values()
print(x)

# items()

x = dict.items()
print(x)

# Check if key exists 

if "name" in dict:
    print("Yes!")

# empty dictionary 

# -------- Change Values ----------- 

dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1945,
    "color": "Black"
}    
print("Before change:", dict)
dict["year"] = 2022
print("After change:",dict)

# update() method

dict.update({"color": "White"})
print(dict)

# Add Items 

dict["fuel"] = "Petrol"
print(dict)

# Removing Items 

# pop()

dict.pop("year")
print(dict)

del dict["color"]
print(dict)

# clear()

dict.clear()
print(dict)

# Loop Through a Dictionary 

dict = {
    "name": "Jiya",
    "age": 48,
    "gender": "Female",
    "designation": "Software Developer"
}

for x in dict:
    print(x)

for x in dict:
    print(dict[x])    

for x in dict.values():
    print(x)    
    
for x in dict.keys():
    print(x)    
    
for x, y in dict.items():
    print(x, y)

# Copy a Dictionary 

# copy()

mydict = dict.copy()
print(mydict)

# dict()

# mydict = dict(dict)
# print(mydict)

# Nested Dictionaries 

department = {
    "student1": {
        "name": "Ankit",
        "age": 22,
        "course": "BTech",
        "branch": "CSE"
    },
    "student2": {
        "name": "Shiv",
        "age": 24,
        "course": "MBA",
        "branch": "IT"
    }
}

print(department)
print(type(department))

# Access Items in Nested Dictionaries

print(department["student1"]["name"])
print(department["student2"]["name"])

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])