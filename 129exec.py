# def reversed(list1):
#     newlist = []
#     for string in list1:
#         newlist.append(string[::-1])
#     return newlist

# newstring = (input("enter string:")).split(" ")
# print(reversed(newstring))

# using list comprehension

# 2
# list = input("enter words comma separated: ").split(",")
# newlist = [string[::-1] for string in list]
# print(newlist)

# 3
def reversed(list1):
    return [string[::-1] for string in list1]
print(reversed(['ab','cd']))    

# newstring = (input("enter string:")).split(" ")
# print(reversed(newstring))