#function : create one function and used in different programs

def add_two(num1, num2):
    return num1 + num2

a = int(input("enter first number: "))
b = int(input("enter second number: "))
total = add_two(a,b)
print (total)

c = (input("enter first name: "))
d = (input("enter second name: "))
print(add_two(c,d))

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 70function.py 
# enter first number: 1
# enter second number: 2
# 3
# enter first name: dharm
# enter second name: patel
# dharmpat  el