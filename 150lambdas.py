# lambda (anonymous function)

add = lambda a, b: a + b
print(add(2,3))

multiply = lambda a, b: a * b
print(multiply(2,3))

def add1(a,b): 
    return a + b

#----------------------------------------------------------------
print(add1)
print(add)
print(multiply)
# add and multiplt does not have any name like function add1 
# <function add1 at 0x000001E82EDEA4D0>
# <function <lambda> at 0x000001E82E903E20>
# <function <lambda> at 0x000001E82EDEA440>