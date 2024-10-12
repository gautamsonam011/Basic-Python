# __iter__() and __next__()

mytuple = ("Apple", "Banana", "Cherry", "Grape")

myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

mystr = "India"
x = iter(mystr)
print(next(x))
print(next(x))
print(next(x))

# Looping through an iterator
for x in mytuple:
    print(x)