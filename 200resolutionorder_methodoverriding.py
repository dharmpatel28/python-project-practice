# method resolution order
# help function is used to for MRO
# print(help(classname)) or classname.mro() or classname.__mro__

# method overriding

class Phone: 
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def fullname(self):
        return f"{self.brand} {self.model}"

class Smartphone(Phone): 
    def __init__(self,brand,model,price,ram):

        super().__init__(brand,model,price)
        self.ram = ram

    # this fullname is overide the function present in phone class
    def fullname(self):
        return f"{self.brand} {self.model} and price is {self.price}"    

d = Phone('oneplus', 7, 2000)
d1 = Smartphone('apple',12,3000,'8gb')  
print(d1.fullname())      