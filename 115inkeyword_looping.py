user_info = {'name' : 'dharm',
             'age' : '21',
             'fav_movie' : ['shershah', 'major'],
             'fav_series' : ['sex education', 'the originals']
}

# check if key exist in dictionary
if 'name' in user_info:
    print(f"1.present")
else:
    print(f"1.not present")

print(" ")

# check if value exist in dictionary       
if 'dharm' in user_info.values():
     print(f"2. value is present")
else:
    print(f"2.value is not present")

print(" ")

# loops in dictionary    
for name in user_info:
    print(f"3. {name}")

print(" ")

for values in user_info.values():
    print(f"4. {values}")

print(" ")

for values in user_info:
    print(f"5.{user_info[values]}")

print(" ")    

# values methods without loop
values = user_info.values()
print(f"6. {values}")        # tuples in list
print(f"6. {type(values)}")

print(" ")

keys = user_info.keys()
print(f"7. {keys}")
print(f"7. {type(keys)}")

print(" ") 

# items methods
user_item = user_info.items()
print(f"8. {user_item}")
print(f"8. {type(user_item)}")

#-------------------------------------output-------------------------------------------------------------

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 115inkeyword_looping.py 
# 1.present
 
# 2. value is present
 
# 3. name
# 3. age
# 3. fav_movie
# 3. fav_series
 
# 4. dharm
# 4. 21
# 4. ['shershah', 'major']
# 4. ['sex education', 'the originals']
 
# 5.dharm
# 5.21
# 5.['shershah', 'major']
# 5.['sex education', 'the originals']

# 6. dict_values(['dharm', '21', ['shershah', 'major'], ['sex education', 'the originals']])
# 6. <class 'dict_values'>

# 7. dict_keys(['name', 'age', 'fav_movie', 'fav_series'])
# 7. <class 'dict_keys'>

# 8. dict_items([('name', 'dharm'), ('age', '21'), ('fav_movie', ['shershah', 'major']), ('fav_series', ['sex education', 'the originals'])])
# 8. <class 'dict_items'>