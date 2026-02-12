# def parameter(firstname, lastname, age):
#     print(firstname)
#     print(lastname)
#     print(age)

# parameter("dharm", "patel", 20)

#output: Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 80default_parameter.py
# dharm
# patel
# 20
    
def parameter(firstname, lastname = "unknown", age = None): # if you set default parameter..
# ....like "lastname"..after "lastname" all parameters should be set
    print(firstname)
    print(lastname)
    print(age)

parameter("dharm")     

# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 80default_parameter.py 
# dharm
# unknown
# None