def sublist(counter):
    count = 0
    for i in counter:
        if type(i) == list:
            count = count + 1
    return count

mixed = [1,2,3,[1,2]]
print(sublist(mixed))

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 106exec.py 
# 1
