
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

# Finally :- 

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")        

try:
    f = open("file.txt")

    try:
        f.write("Hii")
    except:
        print("Something")
    finally:
        f.close()
except:
    print("Something !!")                    