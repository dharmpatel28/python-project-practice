# list comprehension
# with the help of comprehension we can create list in one line

#create a list of square from 1 to 10
square = []
for num in range(1,10):
    square.append(num**2)
print(f"1. {square}")    

# using list comprehension
square = [num**2 for num in range(1,11)]
print(f" 2. list com: {square}")

negative = []
for num in range(1,11):
    negative.append(-num)
print(f"3. {negative}")

# using list comprehension
negative = [-num for num in range(1,11)]
print(f" 4. list com: {negative}")

names = ["dharm", "dhruv", "john"]
letter = []
for name in names:
    letter.append(name[0])
print(f"5. {letter}")

# using list comprehension
letter = [name[0] for name in names]
print(f" 6. list com: {letter}")

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 128list_comprehension.py 
# 1. [1, 4, 9, 16, 25, 36, 49, 64, 81]
#  2. list com: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 3. [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
#  4. list com: [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
# 5. ['d', 'd', 'j']
#  6. list com: ['d', 'd', 'j']