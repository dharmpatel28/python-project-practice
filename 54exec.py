# calculate 1+2+5+6

numbers = (input("enter a number containing 2 or more digit: "))

total = 0
i = 0

while i < len(numbers):
    total = total + int(numbers[i])
    i = i + 1
    print(total) 


# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 53exec.py 
# enter a number containing 2 or more digit: 1256
# 1
# 3
# 8
# 14
