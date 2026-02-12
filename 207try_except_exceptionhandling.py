while True: # this loop is used because , after pass wrong input one time , 
    # it will asked user again to give input

    try: # try block os used where you can find possibility of error
        age = int(input("enter your age:"))
        break      # it break the loop when user give correct answer
    
    except ValueError:
        print("invalid input,try again")

    except: # this will used for another type of error instead of value error 
        print("unexpected error")

if age < 18:
    print("you can't play this game")
else:
    print("you can play this game")