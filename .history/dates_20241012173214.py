# Python Datetime 

# Dates

import datetime

x = datetime.datetime.now()
print(x)

x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

# Creating Date objects 

x = datetime.datetime(2020, 5, 15)
print(x)

# The strtime() Method 

x = datetime.datetime(2018, 7, 1)
print(x.strftime("%B"))

