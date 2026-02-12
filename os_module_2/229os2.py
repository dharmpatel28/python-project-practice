# first enter in os_module_2 folder
import os
import shutil # it can delete folder which is not empty

# filess = os.walk(r'E:\py tutorial\os_module_2')

# for current_path, folder_name, file_name in filess:
#     print(f'current path: {current_path}')
#     print(f'folder name: {folder_name}')
#     print(f'file name: {file_name}')
    

# delete empty folder
# os.rmdir('foldername') # it only delete empty folders    

# create folder inside folder in one step
# os.makedirs('outsidefolder/insidefolder')

# shutil
# shutil.rmtree('outsidefolder') # you have to whole path if you are not in pwd
# shutil.copytree('22folder3', '229folder2/229folder3') # you can copy folder to another folder with changing of name
# shutil.copy('copyfile1.txt','229folder2/copyfile1.txt') # to copy file to another folder
# shutil.move('movefile1.txt','229folder2/movefile1.txt') # to move file to another folder
shutil.move('movefolder1', '229folder2/movefolder1') # to move folder to another folder