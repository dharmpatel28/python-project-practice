# to write , 3 modes is used
# w,a,r+

" w "
# it override the old data and it used when file is empty and 
# you don't want to delete previous data

# w mode create file by their own
with open('215file2.txt', 'w') as f:
    (f.write("file number 2"))

# " a " : "it add new data to file after existing data"

with open('215file2.txt', 'a') as f:
    (f.write("\nappend mode is running.."))

# it also create file by their own
with open('215file2.1.txt', 'a') as f:
    (f.write("\nanother append mode is running.."))

# " r+ ": it did not create file by their own
# it can do both read and write

with open("215file2.2.txt", 'r+') as f:
    f.seek(len(f.read()))
    f.write("\nvery warm day")
