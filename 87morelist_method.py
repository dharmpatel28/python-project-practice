fruits = ["mango", "apple", "orange", "apple" , "banana"]

#count ---------------------------------------------------
print(fruits.count("apple"))

#sort method -----------------------------------------------
fruits.sort()
print(fruits)

# sorted function : it not sort the list instead it print in sorted way ------
print(sorted(fruits))

#clear ------------------------------------------
fruits.clear()
print(fruits)

#copy -------------------------------------------
bike = ["apache", "duke", "bullet", "vespa"]
car1 = bike.copy()
print(car1)

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 87morelist_method.py
# 2
# ['apple', 'apple', 'banana', 'mango', 'orange']
# ['apple', 'apple', 'banana', 'mango', 'orange']
# []
# ['apache', 'duke', 'bullet', 'vespa']