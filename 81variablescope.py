# x = 5 # global variable

# def function():
#     x = 6 #local variable
#     return x

# print(function())
# print(x)

   # Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 81variablescope.py 
# 6
# 5

#--------------------------------------------------------

x = 5               # global variable

def function():
    global x        # to change the value of global variable
    x = 6           #local variable
    return x

print(function())
print(x)

      # Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 81variablescope.py
# 6
# 6
