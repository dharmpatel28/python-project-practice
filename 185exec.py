class Laptop:
    def __init__(self, brand_name, model_name, price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price

l1 = Laptop('HP', 'Pavillion', 70099) #object

print(l1.brand_name)
print(l1.price)

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 185exec.py
# HP
# 70099