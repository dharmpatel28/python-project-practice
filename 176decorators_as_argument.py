from functools import wraps

def only_datatype_allow(datatype):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if all([type(arg)==datatype for arg in args]):
                return function(*args, **kwargs)
            else:
                print("invalid arguments")    
        return wrapper
    return decorator    

@only_datatype_allow(str)
def string(*args):
    string = ''
    for i in args:
        string = string + i
    return string

print(string('dharm', 'patel'))