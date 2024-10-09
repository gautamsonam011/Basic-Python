# Python Loops:- 

# python has two primitive loop commands: 
# while loops 
# for loops 

# The while loop: =>  With the while loop we can execute a set of statements as long as a condition is true

i = 1
while i < 8:
    print(i)
    i += 1

# The break Statement 

i = 1
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1

# The continue statement 

i = 0
while i < 10:
    i += 1
    if i == 4:
        continue
    print(i)

# The else statement 

i = 1
while i < 8:
    i += 1
else:
    print("I is no longer less than 6")        