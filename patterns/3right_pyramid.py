def center_pyramid(numbers):
    space = numbers-1
    print(space)
    for i in range(numbers):
        print(space*" "+i*"*")
        space = space - 1
        
        

center_pyramid(10)