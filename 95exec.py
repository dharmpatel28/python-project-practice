def square_list(numbers):
    square = []
    for i in numbers:
        square.append(i*i)       # i**2 
    return square    

num = list(range(1,11))
print(square_list(num))

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 95exec.py 
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]