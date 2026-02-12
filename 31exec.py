name , character = input("enter name and single character: ").split(",")

print(f"0. user name is {name} and single character is {character}")

print(f"1. {len(name)}")

print(f"2. {name.count(character)}") #for case sensitive 

print(f"3. {name.lower().count(character.lower())}") #for case insensitive

print(f"4. {name.strip().lower().count(character.strip().lower())}") #for case insensitive and 
                                                                    # removing of space insert by user

#output  

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 31exec.py 
# enter name and single character: dharmpAtel,a 
# 0. user name is dharmpAtel and single character is a
# 1. 10
# 2. 1
# 3. 2