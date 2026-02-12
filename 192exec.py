class Laptop:

    count = 0    
        
    def __init__(self, brand_name, model_name, price):
        Laptop.count = Laptop.count + 1
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price

d1 = Laptop('HP', 'Pavillion', 70099)
d2 = Laptop('DP', 'gaming', 21222)


print(Laptop.count)        