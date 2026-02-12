# looping in tuple
mixed = (1,2,3,4)
for i in mixed:
    print(i)
print(" ")    

# tuple with one element
nums = (1) # python considered it as a int , for tuple add " , " after 1 
print(type(nums))
nums1 = (1,)
print(type(nums1))

name = ('dharm') # python considered it as a string , for tuple add " , " after dharm
print(type(name))
name1 = ('dharm',) # python considered it as a string , for tuple
print(type(name1))
print(" ")


#tuple without paranthesis
fruits = 'orange', 'mango'
print(type(fruits))
print(" ")

# tuple unpacking
guitar = ('maneli jami', 'andrew joy')
guitar1 , guitar2 = (guitar) # if 2 name in paranthesis then 2 variables 
                                # have to used not more or less 
print(guitar1)
print(" ")

# list inside tuple
favourite = ('south', ['we made it', 'landscape'])
# you can use function pop, append.. for list inside tuple
favourite[1].pop() # landscape will pop
print(favourite)

# other function of tuple:
# min(), max(), sum 


# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 110moreabout_tuple.py 
# 1
# 2
# 3
# 4
 
# <class 'int'>
# <class 'tuple'>
# <class 'str'>
# <class 'tuple'>
 
# <class 'tuple'>
 
# maneli jami
 
# ('south', ['we made it'])