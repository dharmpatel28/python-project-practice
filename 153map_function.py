# map function are not iterable its iterator 

numbers = [1,2,3,4]
square = tuple(map(lambda i : i**2 , numbers)) # here use lambda function or make a function
print(square)

# using list comprehension

squares = [i**2 for i in numbers]
print(squares)

names = ['dharm', 'john']
length = list(map(len,names))
print(length)

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 153map_function.py 
# (1, 4, 9, 16)
# [1, 4, 9, 16]
# [5, 4]