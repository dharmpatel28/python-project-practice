def cube(a):
    return a**3

l = [1,2,3,4]    

def my_cube(func, l): # l = iterator
    newlist = []
    for item in l:
        newlist.append(func(item))
    return newlist

print(my_cube(cube, l))

# using list comprehension

def my_cube2(func, l): # l = iterator
    return [func(item) for item in l]

print(my_cube2(cube, l))    


# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 166func_As_arg.py
# [1, 8, 27, 64]
# [1, 8, 27, 64]