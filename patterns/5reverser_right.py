def reverse(numbers):
    space = numbers - 1

    for i in range(numbers):
        print(i*' ' + space*"*")
        space = space - 1 
        
        


reverse(10)
