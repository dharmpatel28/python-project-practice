from functools import wraps # because it give corect output for docstrings
def decorator(any_function):
    @wraps(any_function)
    def wrapper(*args, **kwargs):            # *,**
        """ this is wrapper function """
        # print("this is another method....")
        return any_function(*args, **kwargs)  # return
    return wrapper

@decorator    # shortcut
def func1(a):
    print(f"this is a function 1 with argument {a}")
# func1(7)

@decorator
def add(c,b):
    '''this is add function'''
    return c + b

# print(add(3,4))
print(add.__doc__)
print(add.__name__)