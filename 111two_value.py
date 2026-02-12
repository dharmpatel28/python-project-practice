def two_values(a, b):
    add = a + b
    multiply = a * b
    return add, multiply

print(two_values(2,3)) # it will provide tuple like in one paranthesis
add , multiply = two_values(2,3)
print(add)  
print(multiply) # it will print seperated   


# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 111two_value.py
# (5, 6)
# 5
# 6