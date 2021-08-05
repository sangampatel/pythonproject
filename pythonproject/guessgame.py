hidden = 55
def guessgame():
    i = 5
    while i:
        print("No of Turns Left =",i)
        print("Guess The Number In Program(1-100)")
        n = int(input())
        if n == 55:
            print("Yes It Is Right Answer You Won The Game")
            break
        elif n > 100:
            print("You Are Out Of Range Try Again")
        elif n in range(56,101):
            if n in range(56,61):
                print("You Are Very Close To Hidden Number")
            print("Decrese The Number And Try Again\n")
            i = i-1
            if i == 0:
                print("Game Over Restart The Game")
            continue
        elif n in range(1,55):
            if n in range(50,55):
                print("You Are Very Close To Hidden Number")
            print("Increase The Number And Try Again\n")
            i = i-1
            if i == 0:
                print("Game Over Restart The Game")
            continue
guessgame()