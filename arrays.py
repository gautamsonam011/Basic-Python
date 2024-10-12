# Arrays are used to store multiple values in one single variable 

cars = ["Tata", "Mahindra", "Ford"]
print(cars)
print(type(cars))

# Access the elements of an arrays 

x = cars[0]
print(x)

cars[0] = "Toyota"
print(cars)

# The length of an array

# len()

x = len(cars)
print(x)

# Looping array elements 

# for in loop 

for x in cars:
    print(x)

# Adding array elements 

# append() 

cars.append("Honda")   
print(cars) 

# Removing array elements 
# pop() 

cars.pop(2)
print(cars)

# Array Methods:- 
# append()
# clear()
# copy()
# count()
# extend()
# index()
# insert()
# pop()
# remove()
# reverse()
# sort()
