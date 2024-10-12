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