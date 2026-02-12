s = {i**2 for i in range(1,6)}
print(s)

names = set(input("enter name by comma separated: ").split(","))
# names = {'dharm', 'patel'}
first = {name[0] for name in names}
print(first)

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 139sets_comprehension.py
# {1, 4, 9, 16, 25}
# enter name by comma separated: dharm,patel
# {'d', 'p'}