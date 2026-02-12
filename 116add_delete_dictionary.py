user_info = {'name' : 'dharm',
             'age' : '21',
             'fav_movie' : ['shershah', 'major'],
             'fav_series' : ['sex education', 'the originals']
}

# how to add data in dictionary
user_info['phone no.'] = 7096223659
print(user_info)
print(' ')

#how to remove data from dictionary
popitem = user_info.pop('age')
print(popitem)
print(user_info)
print(' ')

#popitem method  : randomly delete any data from dictionary
popped = user_info.popitem()
print(popped)
print(user_info)


# ---------------------------------------------------------------
# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 116add_delete_dictionary.py
# {'name': 'dharm', 'age': '21', 'fav_movie': ['shershah', 'major'], 
# 'fav_series': ['sex education', 'the originals'], 'phone no.': 7096223659}

# 21
# {'name': 'dharm', 'fav_movie': ['shershah', 'major'], 
# 'fav_series': ['sex education', 'the originals'], 'phone no.': 7096223659}

# ('phone no.', 7096223659)
# {'name': 'dharm', 'fav_movie': ['shershah', 'major'], 
# 'fav_series': ['sex education', 'the originals']}