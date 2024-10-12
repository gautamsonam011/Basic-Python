# # json stand of Javascript object notation 

# import json

# # Parse Json 

# # json.loads() method

# x = {"name": "Shiva", "age": 35, "city": "India"}

# y = json.loads(x)
# print(y["age"])

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

