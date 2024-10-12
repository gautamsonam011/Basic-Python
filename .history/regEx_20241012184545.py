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
print(txt)