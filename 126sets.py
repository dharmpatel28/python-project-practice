# set data type
# unordered collection of unique items(can not store repeat variable)

s = {1,2,3,3}
print(f"1. {s}")

l = [1,2,3,4,4,4,4,5,5,5,6,6,7,8,8]      # list
s2 = set(l)                              # convert list to set
s4 = list(set(l))                        # convert set to list
print(f"2. {s2}")                        # set

# methods
s.add(4)
s.remove(2)               # give error when we remove unpresent element from set
s.discard(8)              # can not give error when we remove unpresent element from set
print(f"3. {s}") 

s3 = s2.copy() 
print(f"4. {s3}")

s.clear() 
print(f"5. {s}")

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 126sets.py 
# 1. {1, 2, 3}
# 2. {1, 2, 3, 4, 5, 6, 7, 8}
# 3. {1, 3, 4}
# 4. {1, 2, 3, 4, 5, 6, 7, 8}
# 5. set()