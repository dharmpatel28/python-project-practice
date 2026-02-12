def cube(n):
    cube = {}
    for i in range(1,n + 1):
        cube[i] = i**3                           # cube[i] = key, i**3 = value
    return cube    
        

number = int(input("enter the number:"))
print(cube(number)) 

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 120exec.py 
# enter the number:4
# {1: 1, 2: 8, 3: 27, 4: 64}