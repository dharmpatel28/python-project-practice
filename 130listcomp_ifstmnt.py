numbers = list(range(1,11))

even = [i for i in numbers if i % 2 == 0]
print(even)

# or
# even = [i for i in range(1,11) if i % 2 == 0]
# print(even)

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 130listcomp_ifstmnt.py
# [2, 4, 6, 8, 10]