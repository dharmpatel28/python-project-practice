# how to read and write together

with open("216file1.txt", "r") as rf:
    with open("216file2.txt", "w") as wf:
        wf.write(rf.read())