class NameTooShortError(ValueError): # inherit value error
    pass

def size(name):
    if len(name) < 8:
        raise NameTooShortError("name is too short")

username = input("enter name: ")
size(username)
print(f"hello {username}")