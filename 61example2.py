# 1256 = 1+2+5+6

num = input("enter a number: ")

total = 0

for i in range(0, len(num)):
    total = total + int(num[i])
    print(total)

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 61example2.py 
# enter a number: 1256
# 1
# 3
# 8
# 14    