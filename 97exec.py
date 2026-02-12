def reversed_list(num):

    # 1
    # reversed = []
    # num.reverse()
    # return num

    # 2
    # reversed.append(num[::-1])

    # 3 
    reversed = []
    for i in range(len(num)):
        element = num.pop()
        reversed.append(element)
    return reversed   
    
numbers = list(range(1,5))  
print(reversed_list(numbers)) 

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 97exec.py 
# [4, 3, 2, 1]
