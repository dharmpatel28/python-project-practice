class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        raise NotImplementedError("you have to define a sound method")

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed

d1 = Dog('lucy','doberman')
print(d1.name)
print(d1.sound())        