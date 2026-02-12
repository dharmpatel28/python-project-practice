age = int(input("Enter age: "))

if age == 0 or age < 0 :
    print("Please enter valid age")

elif 1< age <3 :
    print("ticket price = free, free, free")

elif 4< age <10:
    print("ticket price = 100")

elif 11<age <60:
    print("ticket price = 250")
    
else:
    print("ticket price = 200")