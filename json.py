# json stand of Javascript object notation 

import json

# Parse Json 

# json.loads() method

x = {"name": "Shiva", "age": 35, "city": "India"}

# y = json.loads(x)
# print(y["age"])

# Convert from python to json 

# json.dumps() method

x = {
    "name": "Ridhi",
    "age": 50,
    "city": "Unnao"
}

y = json.dumps(x)
print(y)

# we can convert python objects of the following types 

# dict
# list
# tuple
# string
# int
# float
# True
# False
# None

# Format the result 

json.dumps(x, ident = 4)

json.dumps(x, indent=5, separators=(".", "="))

# Order the result 

json.dumps(x, indent=7, sort_keys = True)
