iseven = lambda i : i % 2 == 0
print(iseven(2))

last_char = lambda i : i[-1]
print(last_char("dharm"))

# lambda with if else

length = lambda i: True if len(i) > 5 else False
print(length("abcd"))

# or

length1 = lambda i : len(i) > 5
print(length1("abcdef"))

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 151lambda_practice.py
# True
# m
# False
# True