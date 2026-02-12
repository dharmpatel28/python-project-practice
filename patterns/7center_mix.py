def mix(numbers):
    space = numbers - 1
    
    for i in range(numbers):
        for j in range(space):
            print(end=' ')
        print(i*"* ")
        space = space - 1
            
    space = numbers - 1

    for i in range(numbers):
        for j in range(space):
            print(j*' ' + space*"* ")
            space  =space - 1


mix(5)            
