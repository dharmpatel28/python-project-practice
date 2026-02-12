import os

# print(os.getcwd()) # current working directory # output: E:\py tutorial\os_module_1
# print(os.chdir('path)) # to change the directory

# how to create folders
# (os.mkdir('folder1')) # to create folder , 
# print(os.path.exists('folder1')) # to check whether folder is exists or not
# if os.path.exists('folder1'):
#     print('already exists')
# else:
#     os.mkdir('folder1')    


# how to create files
# open('228file1.txt','a').close() # it did not give error if already exists


# enter whole path if you want to work on another directory
# os.mkdir(r'F:\foldername\filename') # r: for escape SEQUENCE

# to get list of every present files and folders in directory
# print(os.listdir()) # output : ['228file1.txt', '228os1.py', 'folder1']

# if you want list of another directory
# print(os.listdir(r'F:\foldername'))

# to get path of every files and folders in directory
# for item in os.listdir():
#     print(os.getcwd() + "\\" + item)

#another way: it used for every software such mac , linux, windows
for item in os.listdir():
    path = os.path.join(os.getcwd(), item)
    print(path)