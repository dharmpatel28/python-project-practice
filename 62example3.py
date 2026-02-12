name = input("enter name: ")
print(name)

temp_var = ""

for i in range(0, len(name)):
    if name[i] not in temp_var:                # if character is already in temp_var then it will skip the character
        temp_var = temp_var + name[i]                     # to store the character in temp_var
        print(f"{name[i]} : {name.count(name[i])}")



#         Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 62example3.py 
# enter name: dharmd
# dharmd
# d : 2
# h : 1
# a : 1
# r : 1
# m : 1