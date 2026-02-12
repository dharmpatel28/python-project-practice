# all: if any one number is not match with condition then it will give output as false
# any: if any one number is match with condition then it will give output as true

numbers1 = [1, 2, 3, 4, 5]
numbers2 = [6,7,8,9, 10]

even = all([num%2 == 0 for num in numbers1])
print(even)

numbers2 = [6, 7, 11, 9, 13]
even1 = any([num%2 == 0 for num in numbers2])
print(even1)

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 160any_all_function.py 
# False
# True