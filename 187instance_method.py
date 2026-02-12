# object = instance = method

class Person:
    def __init__(self,first_name, last_name,age):  # self is first argument in method of class called object
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def is_age_above(self):
        return self.age > 18
        # or if age > 18:
        #         return eligible

p1 = Person('dharm', 'patel',22)
print(p1.first_name) 
print(p1.fullname())  
print(p1.is_age_above())    