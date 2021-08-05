y = int(input())
def leapyear():
    if y%100==0:
        print("False")
    elif y%400==0:
        print("True")
    elif y%4==0:
        print("True")
    else:
        print("False")
leapyear()