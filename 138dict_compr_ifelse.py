# d = {1 : 'odd', 2 : 'even'}
numbers = {num : ('even' if num % 2 == 0 else 'odd') for num in range(1,6)}
print(numbers)

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ D:/python/python.exe "f:/py tutorial/138dict_compr_ifelse.py"
# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}