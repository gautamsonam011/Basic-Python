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