# print 1 to 10 except 5

for i in range(1,11):
    if i == 5:
        continue                  # when i = 5 loop again goes to for i in.. instead of print (i)
    print(i)



#     Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 63continue.py
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10