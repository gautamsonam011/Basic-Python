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