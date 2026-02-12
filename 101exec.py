def odd_even(num):
    even = []
    odd = []
    for i in num:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i) 
    output = [odd] + [even]  # or    [odd , even]    
    return output

numbers = [1,2,3,4] # list(input("enter list:"))
print(odd_even(numbers))

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 101exec.py
# [[1, 3, 5], [2, 4, 6]]


