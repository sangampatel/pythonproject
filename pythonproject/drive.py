def drive(n):
    if n in range(7,101):
        if n>18:
            print("You Can Drive")
        elif n==18:
            print("Hamko Nahi Pata Aap Physically Aiye(Come Physically)")
        else:
            print("You Cannot Drive")
    elif n in range(0,7):
        print("You Are Small Boy")
    else:
        print("Age Bahut Jyada Hai(Too Much Age)")
print("Enter Your Age")
n = int(input())
drive(n)