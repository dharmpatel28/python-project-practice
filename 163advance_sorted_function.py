fruits = ['mango', 'orange', 'apple']
fruits.sort()
print(fruits)

fruits = ('mango', 'orange', 'apple')
sorted(fruits)
print(fruits) #tuple is immutable so it not sort the fruits

fruits = {'mango', 'orange', 'apple'}
sorted(fruits)
print(fruits) #dict is immutable so it not sort

guitars = [
    {'model' : 'yamaha', 'price' : 8400},
    {'model' : 'tvs', 'price' :56000},
    {'model' : 'hyundai', 'price': 5500}
]

print(sorted(guitars , key = lambda d:d.get('price'), reverse = True)) # reverse will give ans in reverse order
# or
print(sorted(guitars , key = lambda d:d['price']))

# print(min(student, key = lambda item : item.get('age'))['name'])

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 163advance_sorted_function.py
# ['apple', 'mango', 'orange']
# ('mango', 'orange', 'apple')
# {'orange', 'apple', 'mango'}
# [{'model': 'tvs', 'price': 56000}, {'model': 'yamaha', 'price': 8400}, {'model': 'hyundai', 'price': 5500}]
# [{'model': 'hyundai', 'price': 5500}, {'model': 'yamaha', 'price': 8400}, {'model': 'tvs', 'price': 56000}]