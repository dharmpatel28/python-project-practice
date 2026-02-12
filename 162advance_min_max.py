names = ['dharm', 'john', 'jamesh']
print(max(names, key = lambda item : len(item)))
print(min(names, key = lambda item : len(item)))

students = {
    'harshit' : {'score':90, 'age': 12},
    'mohit' : {'score':60, 'age':20},
    'rohit' : {'score':30, 'age': 34}
}

print(max(students, key = lambda item : students[item]['score']))

student = [
    {'name': 'dharmpatel', 'age': 30},
    {'name': 'mohit', 'age':20},
    {'name': 'rohit', 'age': 34}
]
print(min(student, key = lambda item : item.get('age'))['name'])

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 162advance_min_max.py 
# jamesh
# john
# harshit
# mohit