# def cube(num,*args):
#     cubes = []
#     cubes.append(num**3)
#     for digit in args:
#         if args:
#             cubes.append(digit**3)
#         else:
#             print("hey you did not pass any argument")
#     return cubes

# nums = [1,2,3]
# print(cube(1,2,3))    

def cube(num,*args):
    if args:
        return [digit**num for digit in args]
    else:
        return "hey you did not pass any argument"    

nums = [1,2,3]
print(cube(2,*nums))

# 1
# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 143exec.py
# hey you did not pass any argument

# 2
# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 143exec.py 
# [1, 4, 9]