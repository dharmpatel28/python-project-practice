# kwargs: keyword arguments.. double star operator
# it will gather all arguments in dictionary

def func(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} : {v}")

func(first_name = 'John', last_name = 'cena')

print(" ")

def fun(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} : {v}")

info = {'first_names' : 'John', 'age' : 13}
fun(**info) # ** will unpack the dictionary "info"

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 145doublestar_kwargs.py
# first_name : John
# last_name : cena

# first_names : John
# age : 13