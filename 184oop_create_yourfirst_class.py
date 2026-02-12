# how to create an class
# what is init method , or (constructor) in other programming language
# what are attributes, instance variables
# how to create an object

class Person: # first letter is capital
    def __init__(self, first_name, last_name, age): # you can declare anything instead of self
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

# object 
p1 = Person('dharm', 'patel', 21)
p2 = Person('dhruv', 'patel', 24)

print(p1)
print(p1.first_name)

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 184oop_create_yourfirst_class.py
# <__main__.Person object at 0x0000022CEFC9FE20>
# dharm