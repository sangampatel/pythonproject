import random
import time
print("Welcome To Snake  Water & Gun Game")
def swg():
    print("What You Will Choose\n1-Snake 2-Water 3-Gun")
    n = str(input())
    if n == '1':
        print("You Have Choosen Snake\n")
    elif n == '2':
        print("You Have Choosen Water\n")
    elif n == '3':
        print("You Have Choosen Gun\n")
    else:
        print("Invalid Input Restart The Game")
        exit()
    print("Now Computer is Choosing Please Wait\n")
    time.sleep(1)
    y = random.randrange(1,4)
    print("Computer Has Choosen =",y)
    if y == 1:
        print("Computer Have Choosen Snake\n")
    elif y == 2:
        print("Computer Have Choosen Water\n")
    elif y == 3:
        print("Computer Have Choosen Gun\n")
    if n=='1' and y==1:
        print("Match Tie Hogya (Dono Saanp Nikle)\n")
    elif n=='1' and y==2:
        print("You Win Computer Loose (Tumhara Saanp Computer Ka Pani Pi Gaya)\n")
    elif n=='1' and y==3:
        print("You Loose Computer Win (Computer Ne Tumhare Saanp Ko Maar Dala)\n")
    elif n=='2' and y==1:
        print("You Loose Computer Win (Computer Ka Saanp Tumhara Pani Pi Gaya)\n")
    elif n=='2' and y==2:
        print("Match Tie Hogya (Dono Ke Paas Pani Hai)\n")
    elif n=='2' and y==3:
        print("You Win Computer Loose (Computer Ki Gun Tumhare Pani Me Doob Gayi)\n")
    elif n=='3' and y==1:
        print("You Win Computer Loose (Tumne Computer Ke Saanp Ko Bandook Se Maar Dala)\n")
    elif n == '3' and y == 2:
        print("You Loose Computer Win (Tumhari Bandook Computer Ke Pani Me Doob Gayi)\n")
    elif n == '3' and y == 3:
        print("Match Tie Hogya (Dono Ke Paas Bandook Hai)\n")
i = 10
while i:
    print("No Of Games Left =",i)
    swg()
    i = i-1
    if i == 0:
        print("Game Is Completed Restart Game Again")
