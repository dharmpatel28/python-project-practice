# decorators : enhance the functionality of other function
# @ use as decorator

def func1():
    print("this is a function 1")

def func2():
    print("this is a function 2")

# now to enhance the functionality of func1 and func2 without changing the code , 
                        # we have to create another decorator function   

def decorator(any_function):
    def wrapper():
        print("this is awesome function...")
        any_function()
    return wrapper
 
var = (decorator(func1))
var()

#---------------------------------- or-------------------------------
# add decorator above the func1 and func2

def decorator(any_function):
    def wrapper():
        print("this is another method....")
        any_function()
    return wrapper

@decorator    # shortcut
def func1():
    print("this is a function 1")
func1()

@decorator
def func2():
    print("this is a function 2")  
func2()

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 169decorators.py
# this is awesome function...
# this is a function 1

# this is another method....
# this is a function 1
# this is another method....
# this is a function 2
