# what is dictionaries
# it is a unordered collection of data in key : value pair
# we cannot access elements of a dictionary like user[0] because unordered collection

# how to create dictionaries
user = {'name' : 'dharm' , 'age' : '21'}
print(user)
print(type(user))
print( " ")

# 2nd method
user1 = dict(name = 'dharm', age = '21')
print(user1)
print(type(user1))
print( " ")

# how to access to dictionaries elements
print(user['name'])
print(user['age'])
print( " ")

# which type of data dictionaries can store 
# anything
# number, string, list, dict, dictionaries

user_info = {'name' : 'dharm',
             'age' : '21',
             'fav_movie' : ['shershah', 'major'],
             'fav_series' : ['sex education', 'the originals']
}

print(user_info['fav_series'])
print(" ")

# how to add data to empty dictionary

empty = {}
empty['name'] = 'dharmpatel'
empty['age'] = 22
print(empty)

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 114dictionaries.py 
# {'name': 'dharm', 'age': '21'}
# <class 'dict'>

# {'name': 'dharm', 'age': '21'}
# <class 'dict'>

# dharm
# 21

# ['sex education', 'the originals']

# {'name': 'dharmpatel', 'age': 22}