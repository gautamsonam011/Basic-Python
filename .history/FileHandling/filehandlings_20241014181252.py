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