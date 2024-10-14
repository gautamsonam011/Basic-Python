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

class StudentA:
    def __init__(self, name, marks, course):
        self.name = name
        self.marks = marks
        self.course = course
obj = StudentA("Aniket", 56, "Python")
print(obj.name)


class Courses:

    # default constructors 
    def __init__(self):
        pass

    # parameterized constructors 

    def __init__(self, name):
        self.name = name
        print("Adding new data successfully!")

obj1 = Courses("Ram")
print(obj1.name)
