# function with all paramter

#PADK
# P:parameters
# A:*args
# D:Default parameters
# k:**kwargs

def parameters(name, *args, last_name = 'unknown', **kwargs): # parameters should define in this order only
    print(name) 
    print(args)
    print(last_name)
    print(kwargs)

parameters('dharm', 1,2,3, a=1,b=2)    