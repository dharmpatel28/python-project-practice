def two_number(a , b):
    if a > b:
        return a
    
    return b
                                  
                                  # or 

# def  two_number(a,b):
#     return a > b     

number1 = int(input("enter the first number: "))
number2 = int(input("enter the second number: "))
print(two_number(number1, number2))