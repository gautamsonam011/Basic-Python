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
