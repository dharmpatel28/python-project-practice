import random
number = random.randint(0,100)

guess = 1

gnumb = int(input("enter the number between 0 to 100: "))
game_over = False

while not game_over:
    if  gnumb == number:
        print(f"you win and guess in after {guess} try ")
        game_over = True

    else:
        if gnumb < number:
            print("too low")
            guess = guess + 1
            gnumb = int(input("guess again: "))
        else:
            print("too high")
            guess = guess + 1
            gnumb = int(input("guess again: "))
        