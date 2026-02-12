# isinstance method is used to check whether object or instance is of particular class or not
# issubclass method is used to check whether a class is subclass of particular class or not

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

    
    def fullname(self):
        return f"{self.brand} {self.model} and price is {self.price}"    

d = Phone('oneplus', 7, 2000)
d1 = Smartphone('apple',12,3000,'8gb')  

print(isinstance(d,Phone))
print(isinstance(d,Smartphone))

print(" ")
print(issubclass(Smartphone,Phone))
print(issubclass(Phone,Smartphone))
