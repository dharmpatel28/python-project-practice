number = 4

numb = int(input("guess the number: "))
if numb == number:
    print("you win!!")

else:
    if numb > number:
        print("too high")
    else:
        print("too low")