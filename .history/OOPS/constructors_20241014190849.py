# __init__ Function 

class Parent:
    def __init__(self, fullname):
        self.fullname = fullname

obj = Parent("Sonam Gautam")
print(obj.fullname) 

# we can replace self with any other parameter like below

class Employee:
    def __init__(abc, firstname, lastname):
        abc.firstname = firstname
        abc.lastname = lastname

obj = Employee("Ram", "Raj")
print(obj.firstname)
print(obj.lastname)

 