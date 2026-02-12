def multiply(num1 , num2, *args): # we can not write num after the *args
    total = 1
    print(num1) 
    print(num2)
    print(args)
    for i in args:
        total = total * i
    return total    

print(multiply(1,2,3,4))    # argument "1" will assign in num1 and argument "2" will 
                            # assign in num2 and remaining in *args
# compulsarily num1 and num2 should be define if *args is empty then it considered as true 


# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 141argswith_normalparameter.py
# 1
# 2 
# (3, 4)
# 12