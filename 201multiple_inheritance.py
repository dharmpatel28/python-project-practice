class A:
    def a_method(self):
        return 'method a'

    def hello(self):
        return  'hello a'   

class B:
    def b_method(self):
        return 'method b'

    def hello(self):
        return  'hello b'     

class C(A,B):
    pass

class D(B,A):
    pass

a_instance = A()
print(a_instance.a_method())

b_instance = B()
print(b_instance.b_method())

print(" ")

c_instance = C()
print(c_instance.hello())

d_instance = D()
print(d_instance.hello()) 