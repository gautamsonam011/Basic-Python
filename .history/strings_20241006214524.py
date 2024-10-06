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

# Escape Characters \

print("We are the so-called 'Vikings' from the north")

print("I am \"Sonam\", I am 24 years old")

# \'  Single Quote

txt = "It\'s alright."
print(txt)

# \\ Backslash 

txt = "This is a \\(backslash)"

print(txt)

# \n New Line 

txt = "Hello\nWorld!"
print(txt)

# \r  Carriage Return

txt = "Hello\rWorld!"
print(txt)

# \t Tab 

txt = "Hello\tWorld!"
print(txt)

# \b Backspace 
txt = "Hello \b World!"
print(txt)

# \ooo Octal Value 

txt = "\110\145\154\154\157"
print(txt)

# \xhh Hex Value 

txt = "\x48\x65\x6c\x6c\x6f"
print(txt)

# (7):- String Methods:- 

# capitalize() converts the first character to upper

x = "hello"

print(x.capitalize())

# casefold() => converts string into lower case
x = "Sonam"
print(x.casefold())

# Python Booleans : True or False

print(10>9)
print(10 == 9)
print(10 < 9)

a = 200
b = 89

if b > a:
    print("B is greater than A")
else:
    print("B is not greater than A")    

# Evaluate values and variables:- bool() 

print(bool("Hello"))
print(bool(67))    

x = "Sonam"
y = 78

print(bool(x))
print(bool(y))

# Most values are true 

a = bool("ahj")
b = bool(748)
c = bool(["apple", "banana", "cherry"])

print(a)
print(b)
print(c)

# Sonam values are false 
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

class myClass():
    def __len__(self):
        return 0
    
myobj = myClass()
print(bool(myobj))    