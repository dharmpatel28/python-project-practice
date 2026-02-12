# doctrings : it work as a placeholder and write string between ''' and """

def add(a, b):
    ''' this function take 2 number and return their sum'''
    return a + b

# how to print doctrings sentence

print(f"1. {add.__doc__}")

# other inbuilt functions
print(f"2. {sum.__doc__}")
print(f"3. {sorted.__doc__}")

print(" ")

# help functions : get detail about any function

print(f"4. {help(list)}")