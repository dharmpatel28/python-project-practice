def three_number(a , b , c):
    if a > b and a > c:
        return a
    elif b > c and b > a:
        return b
    else:
        return c

number1 = int(input("enter the first number: "))
number2 = int(input("enter the second number: "))
number3 = int(input("enter the third number: "))
print(f"greater number is {three_number(number1, number2, number3)} ")