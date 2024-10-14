# syntax 

f = open("file.txt")

f = open("file.txt", "rt")

# Open a file on the server :- 

f = open("file.txt", "r")
print(f.read())

# f = open("C:\Users\gautam\OneDrive\Desktop\python.txt", "r")
# print(f.read())

# Read only parts of the file 

f = open("file.txt", "r")
print(f.read(2))

# Read Lines 

# readline()

f = open("file.txt", "r")
print(f.readline())

f = open("file.txt", "r")
for x in f:
    print(x)

# Close Files 

f = open("file.txt", "r")
print(f.readline())
f.close()

# File Write/ Create files 

f = open("file.txt", "a")
f.write("Now the file has more content!")
f.close()

# open and read the file after the appending 

f = open("file.txt", "r")
print(f.read())

f = open("file.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

# open and read the file after the overwriting: 

f = open("file.txt", "r")
print(f.read())

# Create a New File 

# open() method 

# f = open("myfile.txt", "x")
# f = open("myfile.txt", "w")

# Delete File 

import os
# os.remove("myfile.txt")

if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("The file does not exist!") 

# Delete Folder 
os.rmdir("myfolder")       