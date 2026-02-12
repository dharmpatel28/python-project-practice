# two same key in dictionaries

user = {'name': 'John', 'age' : 30, 'age': 20}
print(user)
print(user.get('height', 'not found'))

# dharm@Dharm MINGW64 /e/py tutorial
# $ python 119more_get.py 
# {'name': 'John', 'age': 20}
# not found