from functools import wraps
def decorators(functions):
    @wraps(functions)
    def wrapper(*args, **kwargs):
        print(f"you are calling {functions.__name__} function")
        print(f"{functions.__doc__}")
        return functions(*args, **kwargs)
    return wrapper

@decorators
def subtraction(a,b):
    """this function take two number as argument and return their subtraction"""
    return a - b

print(subtraction(4,2))

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 172decorators_practice.py
# you are calling subtraction function
# this function take two number as argument and return their subtraction
# 2