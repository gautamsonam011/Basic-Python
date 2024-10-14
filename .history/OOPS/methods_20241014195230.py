class Sales:  #class
    def __init__(self, product, price):
        self.product = product
        self.price = price

    def Product(self):            # method
        print("This is product name:",self.product ) 

    def Price(self):  # method
        print("This is price:", self.price)


s1 = Sales("Vivo", 56477)
print(s1.Product())
print(s1.Price())


class AverageMarks:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val

        print("Hi", self.name, "your average score is:", sum/3)

obj = AverageMarks("Diya", [45, 78, 38])
print(obj.get_avg()) 

# Static Methods :--------> 

# class level method is static 


class Static:
    @staticmethod
    def hello():
        print("Hello! This is a static method")

print(Static)





