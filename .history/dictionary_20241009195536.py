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