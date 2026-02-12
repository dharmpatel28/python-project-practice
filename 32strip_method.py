
name = "       dharm patel       "

name1 = "      dh ruv  pat el    "

dots = "......"

print(f"1.to remove left side space: {name.lstrip() + dots}")

print(f"2.to remove right side space: {name.rstrip() + dots}")

print(f"3.to remove left and right side space: {name.strip() + dots }")

print(name1.replace(" " , "") + dots) # to remove every space

# output
# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 32strip_method.py 
# 1.to remove left side space: dharm patel       ......
# 2.to remove right side space:        dharm patel......
# 3.to remove left and right side space: dharm patel......
# dhruvpatel......