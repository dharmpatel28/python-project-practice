def center_pyramid(numbers):
    space = numbers-1
    print(space)
    for i in range(1,numbers): # (1-10) also you can write range(numbers) for (0,9)
        for j in range(space):
            print(end = '!')
        print(i*"1 ")
        space = space - 1
        
center_pyramid(10)