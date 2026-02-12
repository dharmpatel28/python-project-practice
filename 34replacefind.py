string = " dharm is a handsome boy and dharm is good in sleeping "

print("1." + string.replace(" " , "_"))
print("2." + string.replace("is" , "was", 1 )) # "1" is a position of is

print(f"3. {string.find('is')}") # position of 1st is
print(f"4. {string.find('is', 8)}") # position of 2nd is

is1 = string.find("is") # position of 1st is
is2 = string.find("is" , is1 + 1) # position of 2nd 
print(f"5. {is2}")


# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 34replacefind.py 
# 1._dharm_is_a_handsome_boy_and_dharm_is_good_in_sleeping_
# 2. dharm was a handsome boy and dharm is good in sleeping 
# 3. 7
# 4. 35
# 5. 35