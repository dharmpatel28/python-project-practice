# make flexible function
# *operator
# *args

# def total(a,b): 
#     return a+b

# print(total(2,3,4)) # we can not pass 3 argument because we have only a and b

def total_args(*args):
    total = 0
    for i in args:
        total = total + i
    return total

print(total_args(1,2,3,4,5)) # here we can pass as many as argument because of * and 
                             # this number will convert into tupple

# note : use args beside * not compulsary but due to python tradition