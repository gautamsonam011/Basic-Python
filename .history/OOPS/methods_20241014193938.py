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


