def conversion(list1):
    integer = []
    for value in list1:
        if (type(value)) == int:
            integer.append(str(value)) # str because we want to store value in form of string in integer
    return integer

list2 = [1,2,3,True,[4,5],("yes", "no")]
print(conversion(list2))  

# def conversion(list1):
#     return [str(value) for value in list1 if type(value) == int or type(value) == float]

# list2 = [1,2,3,True,[4,5],("yes", "no")]
# print(conversion(list2))

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 132exec.py
# ['1', '2', '3']