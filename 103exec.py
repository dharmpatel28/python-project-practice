def common_elem(a , b):
    new_list = []
    for i in a:
        if i in b:
            new_list.append(i)
    return new_list    

list1 = [1,2,3,4]
list2 = [2,3,5]
print(common_elem(list1, list2))


# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 103exec.py 
# [2, 3]