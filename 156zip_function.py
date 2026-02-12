user_id = ['user1' , 'user2', 'user3']
name = ['dharm', 'john', 'james']

print(dict(zip(user_id, name)))

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 156zip_function.py
# {'user1': 'dharm', 'user2': 'john', 'user3': 'james'}

user_id = ['user1' , 'user2', 'user3']
name = ['dharm', 'john', 'james']
last_name = ['patel', 'def', 'gur']

print(list(zip(user_id, name, last_name))) # this will not convert into dictionary because 
# dictionary update sequence element #0 has length 3; 2 is required

# [('user1', 'dharm', 'patel'), ('user2', 'john', 'def'), ('user3', 'james', 'gur')]

