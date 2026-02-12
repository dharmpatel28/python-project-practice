# filter function are not iterable its iterator 

def even(a):
    return a%2 == 0

numbers = [1,2,3,5,8,4,12,9,6]
evens= list(filter(even, numbers))
print(evens)

# or ----------------
evens1 = filter(lambda i : i%2==0, numbers)
print(tuple(evens1)) 

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 154filter_function.py 
# [2, 8, 4, 12, 6]
# (2, 8, 4, 12, 6)