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