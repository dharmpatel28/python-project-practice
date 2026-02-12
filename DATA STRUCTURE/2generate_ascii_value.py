def ascii(key):
    h = 0
    for char in key:
        h = h + ord(char)
    return h % 100

print(f"ascii value or location of key is {ascii('march 8')}")