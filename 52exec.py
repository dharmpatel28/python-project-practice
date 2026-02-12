# sum of n natural number

number = int(input("enter a natural number: "))
print(number)

total = 0
i =1

while i <= number:
    total = total + i
    i = i + 1
    print(total)

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 52exec.py 
# enter a natural number: 6
# 6
# 1
# 3
# 6
# 10
# 15
# 21    