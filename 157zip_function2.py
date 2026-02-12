# how to separate elements from one list to 2

l = [(1,2), (3,4), (5,6), (7,8)]
print(list(zip(*l))) # it will unpack the list l

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 157zip_function2.py
# [(1, 3, 5, 7), (2, 4, 6, 8)]

# how to get a bigger number from 2 list using zip

l1 = [1,2,4,5]
l2 = [0,6,7,8]
newlist = []
for pair in zip(l1,l2):
    print(pair)
    newlist.append(max(pair))
print(newlist)

# [1, 6, 7, 8]