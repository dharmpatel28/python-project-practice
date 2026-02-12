# in keyword and for loop in sets

s = {'a' , 'b' , 'c'}

if 'a' in s:
    print("present")
else:
    print("not present")


for i in s:
    print(i)

# union(|) and intesection(&)

s1 = {1,2,3,4}
s2 = {3,4,5,6}

union = s1 | s2
print(union)

intersection = s1 & s2
print(intersection)

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 127moreabout_sets.py
# present
# b
# a
# c
# {1, 2, 3, 4, 5, 6}
# {3, 4}