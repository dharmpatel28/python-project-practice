
#---------------------------------- or-------------------------------
# add decorator above the func1 and func2

def decorator(any_function):
    def wrapper(*args, **kwargs):            # *,**
        print("this is another method....")
        return any_function(*args, **kwargs)  # return
    return wrapper

@decorator    # shortcut
def func1(a):
    print(f"this is a function 1 with argument {a}")
func1(7)

print(" ")

@decorator
def add(c,b):
    return c + b

print(add(3,4))