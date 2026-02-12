# also called clousure and first class function

def outer():
    def inside():
        print("inside function")
    return inside

var = outer() # outer
var() # inner

#----------------------------------------------------------------

def outer2(msg):
    def inner2():
        print(f"message is {msg}")
    return inner2()

var = outer2("hello sunday.. ")        

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 167func_return_function.py
# inside function
# message is hello sunday..