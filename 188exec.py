# class Laptop:
#     def __init__(self, brand_name, model_name, price, offer):
#         self.brand_name = brand_name
#         self.model_name = model_name
#         self.price = price
#         self.offer = offer

#     def calculate(self):
#         return self.price - (self.offer/100 * self.price)
    
# d1 = Laptop('HP', 'Pavillion', 70000, 20)
# print(d1.offer)
# print(d1.calculate())

#---------------------or--------------------------------------

class Laptop:
    def __init__(self, brand_name, model_name, price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price

    def calculate(self,num):
        return self.price - ((num/100) * (self.price))
    
d1 = Laptop('HP', 'Pavillion', 70000)
print(d1.calculate(50))