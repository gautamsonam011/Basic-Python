# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

import re

txt = "The rain in Spain"
x = re.search("The. *Spain$", txt)

if x:
    print(txt)
else:
    print("Not Exist!")    