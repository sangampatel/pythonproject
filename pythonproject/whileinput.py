def whileinput():
    while 1:
        print("Enter The Number")
        n = int(input())
        if n < 100:
            print("Number Is Less Than 100 Try Again")
            continue
        elif n ==100:
            print("You Entered Excatly 100 Try Again")
            continue
        else:
            print("Congratulation You Finally Entered Number Greater Than 100")
            break
whileinput()

