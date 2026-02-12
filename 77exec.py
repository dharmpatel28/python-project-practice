def is_palindrome(string):
    return string == string[-1::-1]
   
string1 = input("enter a string: ")    
print(is_palindrome(string1))

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 77exec.py 
# enter a string: dhahd
# True