def revesed_list(word):
    reversed = []
    for i in word:
        reversed.append(i[::-1])
    return reversed    
       
#string = ["abc" , "xyz"] 
string = (input("enter words: ")).split(" ")
print(revesed_list(string))  

# output
# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 99exec.py 
# enter words: abc xyz
# ['cba', 'zyx']