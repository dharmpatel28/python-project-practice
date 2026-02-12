class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def fullname(self):
        return f"{self.brand} {self.model}"

    def __add__(self,other): # another function is sub,mul,etc....
        return self.price + other.price

details = Phone('apple',12,2000)
details2 = Phone('apple',13,4000)

print(details + details2)