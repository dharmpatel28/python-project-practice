# can we derive more than one class from base class

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

class Smartphone2(Phone): 
    def __init__(self,brand,model,price,ram,camera):

        super().__init__(brand,model,price)
        self.ram = ram
        self.camera = camera


d2 = Smartphone2('samsung',7,30000,'8gb','30mp')

print(d2.fullname())   

