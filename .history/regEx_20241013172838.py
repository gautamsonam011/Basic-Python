# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
    print(txt)
else:
    print("Not Exist!")    

# The findall() function 

# findall() 

txt = "It is a findall function"
x = re.findall("fin", txt)
print(x)    

# The search() function 

txt = "The rain in spain"
x = re.search("\s", txt)

print(x.start())

txt = "The rain in spain"
x = re.split("\s", txt)
print(x)

# The sub() function 
# sub()

txt = "Hi guys how are you!"
x = re.sub("\s", "9", txt)
print(x)

x = re.sub("\s", "9", txt, 2)
print(x)

# Match Object:- 

x = re.search(r"\bS\w+", txt)
print(x.span())

x = re.search(r"\bS\w+", txt)
print(x.string)

x = re.search(r"\bS\w+", txt)
print(x.string)
