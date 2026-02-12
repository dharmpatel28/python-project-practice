def reverse(numbers):
    space = numbers - 1

    for i in range(numbers):
        for j in range(space):
            print(j*' ' + space*"* ")
            space  =space - 1      
        


reverse(6)        