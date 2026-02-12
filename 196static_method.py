class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

#static method

@staticmethod
def hello():
    print("hello static  method called..")

d1=Person.hello()
print(d1.name)