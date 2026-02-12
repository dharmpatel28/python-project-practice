class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def fullname(self):
        return f"{self.brand} {self.model}"

    # str and repr methods: this is used to print object 
    # __len__ method

    def  __str__(self): # user method
        return f"{self.brand} {self.model}"

    def  __repr__(self): # developer method..  so that they can debug it
        return f'Phone(\'{self.brand} {self.model}\', and price is {self.price})'

    def  __len__(self):
        return len(self.fullname())

details = Phone('apple', 12,3000)
print(details) # this will not print the output until __str__ or __repr__ is used
print(" ")

print(str(details)) #another method 
print(" ")

print(repr(details))
print(" ")

print(details.__repr__()) # another method
print(" ")

print(len(details))