def divide(a,b):
    return a/b

while True:
    try:
        num1,num2 = (input("Enter two number: ").split(","))
        break

    except ValueError:
        print("please input numbers only..")

    except ZeroDivisionError:
        print("please don't divide by zero")

print(divide(int(num1),int(num2)))

# def divide(a,b):
#     try:
#         return a/b

#     except ZeroDivisionError:
#         print("please don't divide by zero")
#     except TypeError:
#         print("please input numbers only")

# print(divide(4,"2"))