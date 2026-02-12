def average(*args):
    averages = []
    for pair in zip(*args): # this will first digit of every list because of zip function
        averages.append(sum(pair)/len(pair))
    return averages

print(average([1,2,3], [4,5,6] , [7,8,9]))

# or

average = lambda *args : [sum(pair)/len(pair) for pair in (args)]#this will print using pair
print(average([1,2,3], [4,5,6] , [7,8,9]))

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 158advance_function_practice.py
# [4.0, 5.0, 6.0]
# [2.0, 5.0, 8.0]