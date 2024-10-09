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