# There are two types of data types 
# Mutable and Immutable 

# String data type Immutable

x = "This is a Basic Python Course"
print(type(x))  #<class 'str'>

# Integer data type Immutable

x = 465
print(type(x)) #<class 'int'>

# float data type Immutable 

y = 46.78
print(type(y)) #<class 'float'>

# Complex data type 

z = 1j
print(type(z))

# z = 2i this is not support in python

# List data type mutable

x = [3,5, "Hello", 576.78, -43, 0, True]

print(type(x))

# Tuple data type Immutable

x = (54, 67, 78.32, True, "Python")

print(type(x))

# Range data type 

x = range(23, 80)
print(type(x))

# Dictionary data type mutable

x = {
    "name": "Sonam Gautam",
    "age": 24,
    "designation": "Software Developer"
}
print(type(x))

# Set data type 

x = {34, "apple", 56, True, 56.87}
print(type(x))

# Frozenset data type 

x = frozenset({"apple", "banana", "cherry"})
print(type(x))

# Boolean Data Type 

x = True
y = False
print(type(x))
print(type(y))

# Bytes data type 

x = b"Hello World"
print(type(x))
print(x) 

# bytesarray data type

x = bytearray(56)
print(type(x))
print(x)

# memoryview data type 

x = memoryview(bytes(57))
print(type(x))

# non type data type 

x = None
print(type(x))


# Python Numbers 

# There are three numeric types in python 

x = 23
y = 67.89
z = 3+5j

print(type(x))
print(type(y))
print(type(z))