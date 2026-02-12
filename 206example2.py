class Mobile:
    def __init__(self,name):
        self.name = name

class Mobilestore:
    def __init__(self):
        self.mobiles = []

    def add_mobiles(self,new_mobiles):
        if isinstance(new_mobiles,Mobile):
            self.mobiles.append(new_mobiles)
        else:
            raise TypeError("mobile should be object of mobile class")

d1 = Mobile('samsung')
d2 = Mobilestore()
samsung = 'samsung galaxy'
d2.add_mobiles(samsung)

print(d1.name)
print(d2.mobiles)