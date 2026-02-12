name = input("Enter name: ")

temp_var = ""

i = 0

while i < len(name):

    if name[i] not in temp_var:

        temp_var = temp_var + name[i]
        # print(temp_var)

        print(f" character {name[i]} is repeat {name.count(name[i])} times in string ")

    i = i + 1

#     Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 56exec.py 
# Enter name: dharm patel
#  character d is repeat 1 times in string 
#  character h is repeat 1 times in string
#  character a is repeat 2 times in string
#  character r is repeat 1 times in string
#  character m is repeat 1 times in string
#  character p is repeat 1 times in string
#  character t is repeat 1 times in string
#  character e is repeat 1 times in string
#  character l is repeat 1 times in string