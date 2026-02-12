user_info = {'name' : 'dharm',
             'age' : '21',
             'fav_movie' : ['shershah', 'major'],
             'fav_series' : ['sex education', 'the originals']
}

more_info = {'name': 'dharm patel' , 'state' : 'gujarat'}

user_info.update(more_info)
print(user_info)

# name from more_info overwrite the user_info and data of more_info add to user_info

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 117update_dict.py
# {'name': 'dharm patel', 'age': '21', 'fav_movie': ['shershah', 'major'],
#  'fav_series': ['sex education', 'the originals'], 'state': 'gujarat'}