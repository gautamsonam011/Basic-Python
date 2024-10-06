#(1):- single quotation and double quotation 

print("Hello World!")
print('Hello World!')

# Quotes inside quotes 

print("He's a software 'engineer' ")
print('I am a "software developer" ')

# Multiline strings 

a = """

Hi
Guys!
Welcome to python course!
"""

print(a)

# (2):- Slice Strings 

x = "Hello World"

print(x[2:5])

# Slice from the start 

print(x[:6])

# Slice to the end 

print(x[3:])

# Negative Indexing 

print(x[-6:-3])

# (3):- Modify Strings 

# Upper Case:- upper()

print(x.upper())

# Lower Case:- lower()

print(x.lower())

# Remove whitespace: - strip()

print(x.strip())

z = "  Hey! G"
print(z.strip())

# Replace String:- replace()

a = "Hello, World!"

print(a.replace("H", "Ji"))

# Split String :- split() method returns a list

b = "Hello World"

print(a.split(","))

# (4):- Concatenate Strings 

a = 57
b = "Hello"
# c = a + b
# print(c)  unsupported operand type(s) for +: 'int' and 'str'

d = "World"

print(b+d) 

# Format Strings :-- format()

age = 34
# t = "My name is Sonam, I am" + age  can only concatenate str (not "int") to str
# print(t)

print(f"My name is sonam gautam, i am {age}")

price = 700
txt = f"The price is {price} Rs"
print(txt)

print(f"The price is {price: .2f}Rs")

print(f"The price is {20 * 43}Rs")