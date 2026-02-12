def reverse(numbers):
    length = numbers - 1
    print(length)

    for i in range(numbers):
        print(length*"*")
        length = length - 1

reverse(10)