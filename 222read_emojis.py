# # how to read emojis
# with open("222file1.txt", 'r', encoding='utf-8') as rf: # encoding='utf-8' : read emojis
#     print(rf.encoding)
#     data = rf.read()
#     print(data)

# how to read long file in small parts
with open("222file2.txt", 'r') as f:
    data = f.read(10)
    while len(data) > 0:
        print(data)
        data = f.read(10) # 10 words at a time