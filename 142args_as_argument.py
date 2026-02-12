def multiply(num1 , num2, *args): # we can not write num after the *args
    total = 1
    print(args)
    for i in args:
        total = total * i
    return total    

nums = [2,3,4,2]  # or (2,3,4)
print(multiply(*nums)) # here * will unpack the [2,3,4,2] so it will not give error 

# to use the nums we have to define * in argument