# list vs string

# string are immutable(can't change original string)
string = " dharm"
print(string.title())                               # create new string but can't change original
print(string)

# list is mutable(change)
list = ["dharm", "dharm1", "dharm2", "dharm3"]
list.pop()                                          # change original list
print(list)