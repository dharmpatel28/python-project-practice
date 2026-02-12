def add(a,b):
    if type(a) == int and type(b) == int:
        return a + b
    raise TypeError("oops you are passing wrong datatype to function")

print(add('1','2'))
