class Phone: # base class/ parent class
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def fullname(self):
        return f"{self.brand} {self.model}"

class Smartphone(Phone): # "phone is written to inherit in smartphone"
    def __init__(self,brand,model,price,ram,camera):

        #method 1:
        # Phone.__init__(self,brand,model,price)
        # self.ram = ram
        # self.camera = camera

    # no need to describe method for fullname because it inherit from phone class

        #method 2:
        super().__init__(brand,model,price)
        self.ram = ram
        self.camera = camera

d1 = Phone('apple',12,70000)
d2 = Smartphone('oneplus',7,30000,'8gb','30mp')

print(d1.fullname())
print(d2.fullname())   
print(d2.price)
print(d2.ram) 
