
try:
    print(x)
except:
    print("An Exception occurred")    

# Many Exception:- 

try:
    print(x)
except NameError:
    print("Variable x is not defined")  

except:
    print("Something else went wrong")   

# Else 

try:
    print("Hello")
except: 
    print("Something went wrong")

else:
    print("Nothing went wrong")    
