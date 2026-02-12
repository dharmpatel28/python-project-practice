def reverse(*args):
    names = []
    for name in args:
        for i in name:
            names.append(i[::-1].title())
    return names            

user = ('dharm', 'patel')
print(reverse(user))

# def reverse(l, **kwargs):
#     if kwargs.get('reverse_str') == True: 
#         return [name[::-1].title() for name in l] 
#     else: 
#         return [name.title() for name in l]   

# user = ('dharm', 'patel')

# print(reverse(user))
# print(reverse(user, reverse_str = True))
