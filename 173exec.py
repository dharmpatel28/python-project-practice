from functools import wraps
import time
def calculate_time(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        print(f"executing function : {function.__name__}")
        t1 = time.time()
        returned_value = function(*args, **kwargs)
        t2 = time.time()
        total = t2 - t1
        print(f"this function took {total} seconds to run")
        return returned_value   
    return wrapped

@calculate_time
def subtraction(a,b):
    return a - b

print(subtraction(4,2))

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 173exec.py 
# executing function : subtraction
# this function took 0.0 seconds to run
# 2