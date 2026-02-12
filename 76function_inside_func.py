def two_number(a , b):
    if a > b:
        return a
    
    return b

def new_greatest(a,b,c):
    #bigger = two_number(a , b)
    return two_number(two_number(a , b) , c)

number1 = int(input("enter the first number: "))
number2 = int(input("enter the second number: "))
number3 = int(input("enter the third number: "))
print(f" greater is {new_greatest(number1 , number2, number3)}")