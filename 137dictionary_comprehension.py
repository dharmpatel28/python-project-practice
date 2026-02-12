# square ={1:1, 2:4. 3:9}

square ={f" the square of {num} is {num**2}" for num in range(1,6)}
for i in square:
    print(f"{i}")

# count character

string = input("enter string: ")
counting = {char : string.count(char) for char in string}
print(counting)    

# $ python 137dictionary_comprehension.py
#  the square of 2 is 4
#  the square of 3 is 9
#  the square of 1 is 1
#  the square of 4 is 16
#  the square of 5 is 25

# enter string: dharmpatel
# {'d': 1, 'h': 1, 'a': 2, 'r': 1, 'm': 1, 'p': 1, 't': 1, 'e': 1, 'l': 1}