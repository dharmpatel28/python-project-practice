numbers = [1,2,3,4]
print(f" 1. {numbers}")
print(f" 2. {numbers[1]}")

words = ["one", "two", "three", "four"]
print(f" 3. {words}")
print(f" 4. {words[:3]}")

mixed = [1,2,3,4, "five", "six", "seven", "dharm"]
print(f" 5. {mixed}")
print(f" 6. {mixed[-1]}")

mixed[7] = "patel"
print(f" 7. {mixed}")

# output: 
# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 82list.py
#  1. [1, 2, 3, 4]
#  2. 2
#  3. ['one', 'two', 'three', 'four']
#  4. ['one', 'two', 'three']
#  5. [1, 2, 3, 4, 'five', 'six', 'seven', 'dharm']
#  6. dharm
#  7. [1, 2, 3, 4, 'five', 'six', 'seven', 'patel']