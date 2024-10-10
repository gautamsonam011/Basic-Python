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