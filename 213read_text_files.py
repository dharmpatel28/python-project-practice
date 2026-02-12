#read file
# open function
# read method : it gives data of file in form of string
# tell method : it used to find cursor position
# seek method : to change the position of cursor
# readline method : it used to print only oneline
# readlines method : it print data in list
# close method

# f = open('filename', 'mode') default mode is r
# f = open('213file1.txt')
# print(f" cursor position {f.tell()}")
# print(f.read())
# print(f" cursor position {f.tell()}")
# print(f"after seek method pos. of cursor is : {f.seek(0)}")
# f.close()

# f = open('213file1.txt')
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close()

# f = open('213file1.txt')

# lines = f.readlines()
# # print(lines)
# # print(len(lines))

# # or
# lines = f.readlines()
# for line in lines:
#     print(line , end = "")

# or
# lines = f.readlines()
# for line in f.readlines()[:2]: # this will print only 2 lines
#     print(line , end = "")

# f.close()

# f = open('213file1.txt')
# print(f.name)
# print(f.closed)
# f.close()
# print(f.closed)

# f = open(r'G:\newfolder\file1.txt') 
# # here r is because python considered \n of \newfolder as escape sequence
# # you have to write full path if your file present in anothe folder
# print(f.name)
# print(f.closed)
# f.close()
# print(f.closed)