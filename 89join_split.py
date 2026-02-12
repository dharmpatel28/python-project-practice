# split : convert string to list --------------------------

name = "dharm patel , dhruv"  # string
print(name.split(" \, "))

name1 = "dharm patel".split()
print(name1)

# join : convert list to string ---------------------------

name = ["dharm" , "dhruv", "patel"] # list
print(",".join(name))

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 89join_split.py 
# ['dharm patel , dhruv']
# ['dharm', 'patel']
# dharm,dhruv,patel