# json stand of Javascript object notation 

import json

# Parse Json 

# json.loads() method

x = {"name": "Shiva", "age": 35, "city": "India"}

y = json.loads(x)
print(y["age"])

# Convert from python to json 

# json.dumps() method

x = {
    "name": "Ridhi",
    "age": 50,
    "city": "Unnao"
}

y = json.dumps(x)
print(y)
