class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = max(price,0) # to set min price
        # if price > 0:
        #     self.price = price
        # else:
        #     self.price = 0
         
    def specification(self):
        return f"{self.brand} {self.model} price is {self.price}"     

d1 = Phone('apple', 12,-700000) #"-""
print(d1.price)
d1.price = -11111
print(d1.price)

print(d1.specification())        