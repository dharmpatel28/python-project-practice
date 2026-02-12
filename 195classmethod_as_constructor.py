#  ------create own constructor --------------------------------    
    
class Laptop:

    # count = 0    
        
    def __init__(self, brand_name, model_name, price):
        # Laptop.count = Laptop.count + 1
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price

    def fullname(self):
        return f"{self.brand_name} {self.model_name}"    


# ------create own constructor --------------------------------

    @classmethod
    def string(cls,string):
        first,last,age=string.split(",")
        return cls(first,last,age)

d1 = Laptop('HP', 'Pavillion', 70099)

d2 = Laptop.string('dharm,patel,20')
print(d2.fullname())
