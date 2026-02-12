def word(string):
    name = {}
    for i in string:
        name[i] = string.count(i)
    return name    

words = input("enter words: ")
print(word(words))

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 122wordcount_dict.py 
# enter words: dharm patell
# {'d': 1, 'h': 1, 'a': 2, 'r': 1, 'm': 1, ' ': 1, 'p': 1, 't': 1, 'e': 1, 'l': 2}