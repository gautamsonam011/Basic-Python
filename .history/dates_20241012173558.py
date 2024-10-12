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

# %w 

x = datetime.datetime.now()    #Weekday as a number 0-6, 0 is Sunday
print(x.strftime("%w"))

# %d Day of month 01-31 

print(x.strftime("%d"))

# %b Month name, short version	Dec
print(x.strftime("%b"))