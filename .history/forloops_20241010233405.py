# For Loops 

students = ["Sonam", "Ankit", "Raj", "Gautam"]
for x in students:
    print(x)
    
# Looping Through a string 

for x in "Sonam":
    print(x)

# The break statement 

for x in students:
    print(x)

    if x == "Ankit":
        break

for x in students:
    if x == "Ankit":
        break
    print(x)    

# The continue statement 

for x in students:
    if x == "Raj":
        continue
    print(x)    

# The range() function 

for x in range(8):
    print(x)    

for x in range(2, 8):
    print(x)    
    
for x in range(1, 10, 2):
    print(x)    


# Else in for loop 

for x in range(10):
    print(x)
else:
    print("Finally finished!")    

for x in range(10):
    if x == 5: 
        break
    print(x)  

else:
    print("Finally finished!")      

# Nested Loops :- 

x = [4, 6, 8, 2]
y = [8, 9, 3, 5]

for i in x:
    for j in y:
        print(i, j)
