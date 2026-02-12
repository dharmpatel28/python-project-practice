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

class Smartphone2(Smartphone): # "Smartphone2 get everything, what smartphone have" 
    def __init__(self,brand,model,price,ram,camera):

        super().__init__(brand,model,price,ram)
        self.camera = camera