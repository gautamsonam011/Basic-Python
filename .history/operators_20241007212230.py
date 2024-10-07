# (1):- Arithmetic Operators 
# Addition (+) 

x = 9
y = 3
z = x+y
print(z)

# Subtraction (-) 

z = x - y
print(z)

# Multiplication (*) 

z = x * y
print(z)

# Division (/) 

z = x/y
print(z)

# Modulus (%) 

z = x % y
print(z)

# Exponentiation (**)

z = x ** y
print(z)

# Floor division (//)
x = 6
y = 2
z = x // y

print(z)

# Python Assignment Operators 

# (=)
x = 8
print(x)

# (+=) 

x += 8  # x = x+8
print(x)

# (-=)

x -= 7 # x = x - 7
print(x)

# (*=)

x *= 4 # x = x * 4
print(x)

# (/=)

x /= 3 # x = x / 3
print(x)

# (%=)

x %= 3 # x = x % 3
print(x)

# (//=)

x //= 3 # x = x // 3
print(x)

# (**=)

x **= 3 # x = x**3
print(x)

# (&=)

# x &= 3.0 # x = x & 3
# print(x)

# (|=)

# x |= 3 # x = x | 3

# print(x) unsupported operand type(s) for |=: 'float' and 'int'

# (^=)

# x ^= 3 # x = x ^ 3
# print(x) unsupported operand type(s) for ^=: 'float' and 'int'

# (>>=)

# x >>= 3 # x = x >> 3

# print(x)

# (<<=)

# x <<= 4 # x <<= 4

# print(x)

# # (:=)

# print(x:=4)

# Python Comparsion Operators :- 

# Equal (==)

x = 8
y = 8 
z = x == y
print(z)

# Not equal (!=)

x = 7
y = 3
z = x != y
print(z)

# Greater thaan (>) 

x = 7
y = 5
print(x > y)

# Less than (<)
x = 7
y = 5
print(x < y)

# Greater than or equal to (>=)

print(x >= y)

# Less than or equal to (<=)
print(x <= y)


# Python Logical Operators 

# and 

x = 5
y = 3

z = x and y
print(z)

z = (x > y) and (y < x)
print(z)

# or 

z = (x < y) or (x > y)
print(z)

# not

z = not(x == y) 
print(z)

# Python Identity Operators

# is 

x = ["Sonam", "Raj"]
y = ["Shiv", "Radha", "Raj"]

z = x

print( x is y)

print(x == y)

x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is y) # returns False because x is not the same object as y, even if they have the same content

z = x
print( x is z)  # returns True because z is the same object as x

print( x is not z)
print(x is not y)

print(x != y)

# Membership operators

x = ["python", "java", "html"]

print("python" in x)

print("python" not in x )

print("css" not in x )

# Bitwise operators 

# & (AND)

print(6 & 7) 

print( 5 | 7)
print(3 ^ 7)
print(~6)
