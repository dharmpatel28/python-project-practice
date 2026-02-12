class Circle:

    pi = 3.14 # class variable.. 
    # CV is used when same value is used for multiple times to avoid storage wastage

    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * Circle.pi * self.radius # circle.pi because it is class variable

number = int(input("enter the number:"))
d1 = Circle(number)
print(d1.circumference())   