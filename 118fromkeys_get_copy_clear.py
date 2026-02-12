# from keys
key = dict.fromkeys(['name' , 'age', 'gender'], 'unknown')
print(f"1. {key}")

key1 = dict.fromkeys('abc', 'unknown')
print(f"2. {key1}")

key2 = dict.fromkeys(range(1,6), 'unknown')
print(f"3. {key2}")

key3 = dict.fromkeys(['name' , 'age'], ['unknown' , 19])
print(f"4. {key3}")

# get 
print(f"4. {key.get('name')}")

if key.get('name'):
    print(f"5.present")
else:
    print(f"5.not present")    

# copy
d = {'name' : 'dharm', 'age' : 21 }
d1 = d.copy()
print(f"6.{d1}")            #  d1 and d are both different dictionary
print(f"7.{d}")             # if we describe d1 = d then d1 and d are same
print(f"8.{d is d1}") 

# clear 
d.clear()
print(f"9.{d}")
