class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = max(price,0) # to set min price
        
    def specification(self):
        return f"{self.brand} {self.model} price is {self.price}"     \
                
# restrict user from entering negative price 
    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, new_price):
        self.price = max(new_price,0) 

d1 = Phone('apple', 12,-700000) #"-""
print(d1.price)
d1.price = -11111
print(d1.price)

print(d1.specification())   