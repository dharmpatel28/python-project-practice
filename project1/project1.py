import os , shutil

# audio = ('.mp3', '.m4a')
# video = ('.mkv', '.mpeg')
# image = ('.png', '.jpg')

# folderpath = input("enter folderpath: ")

# def fileseparator(folderpath, filextension):
#     files = []
#     for file in os.listdir(folderpath):
#         for extension in filextension:
#             if file.endswith(extension):
#                 files.append(file)
#     return files            
# print(fileseparator(folderpath,audio))    

#--------------------------------------------------------------#
folderpath = input("enter folderpath: ")

dict_extension = {
    'audio' : ('.mp3', '.m4a'),
    'video' : ('.mkv', '.mpeg'),
    'image' : ('.png', '.jpg'),
}

def fileseparator(folderpath, file_extension):
    files = []
    for file in os.listdir(folderpath):
        for extension in file_extension:
            if file.endswith(extension):
                files.append(file)
    return files            
# print(fileseparator(folderpath,audio))

#folder
for key,value in dict_extension.items():
    foldername = key.split('_')[0] + 'files'
    folderpath1 = os.path.join(folderpath, foldername)
    os.mkdir(foldername)

#files        
    for item in fileseparator(folderpath, value):
        item_path = os.path.join(folderpath, item) # file want to transfer
        folderpath2= os.path.join(folderpath1,item) # destination folder
        shutil.move(item_path, folderpath2)