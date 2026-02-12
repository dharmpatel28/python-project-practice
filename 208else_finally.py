while True: 
    try: 
        age = int(input("enter your age:"))
        
    except ValueError:
        print("invalid input,try again")

    except:
        print("unexpected error")

    else: # this statement is run when there is no exception ..
    #or for another statement which can be used in try block   
        print(f"user input is : {age}")
        break
    
    finally: # finally block will always run either there is error or no error and.. 
        # it run before the break statement
        # it used when we have to write code which compulasary needed to run  
        print("finally statement")
