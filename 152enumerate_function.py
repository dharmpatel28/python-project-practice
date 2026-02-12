names = ['abc', 'abcd', 'dharm']
for pos , name in enumerate(names):
    print(f"{pos}-->{name}")

def find_pos(l,target):
    for pos,name in enumerate(l):
        if name == target:
            return pos
    return -1

l = ['a','b']
print(find_pos(l,'b'))

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 152enumerate_function.py 
# 0-->abc
# 1-->abcd
# 2-->dharm
# 1