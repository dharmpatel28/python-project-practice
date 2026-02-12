# from functools import wraps
# def only_int_allow(functions):
#     @wraps(functions)
#     def wrapper(*args, **kwargs):
#         data_types = []
#         for arg in args:
#             data_types.append(type(arg)==int)
#         if all(data_types):
#             return functions(*args, **kwargs)
        # else:
        # print("invalid arguments")

#     return wrapper

# def add(*args):
#     total = 0
#     for i in args:
#         total = total + i
#     return total

# print(add(1, 2, 3, 4, 5))

    # or ----------------------------------------------------------------

from functools import wraps
def only_int_allow(functions):
    @wraps(functions)
    def wrapper(*args, **kwargs):
        if all([type(arg)==int for arg in args]):
            return functions(*args, **kwargs)
        else:
            print("invalid arguments")    
    return wrapper        

@only_int_allow
def add(*args):
    total = 0
    for i in args:
        total = total + i
    return total

print(add(1, 2, 3, 4, 5))

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 175decorators_practice.py 
# 15