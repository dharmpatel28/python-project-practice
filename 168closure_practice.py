def power(x):
    def number(n):
        return n**x
    return number

cube = power(3)
print(cube(2))

square = power(2)
print(square(5))

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 168closure_practice.py 
# 8
# 25