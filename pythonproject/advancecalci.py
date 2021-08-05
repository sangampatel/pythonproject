def wlc():
    print("Welcome To Sangam Advance Calculator")
wlc()
def inp():
    global a
    global b
    a = float(input("Enter The Value Of a\n"))
    b = float(input("Enter The Value Of b\n"))
def op():
    print("What Operation You Want +,-,*,/")
op()
n = str(input())
# def maininp():
#     global n
#     n = str(input())
# maininp()
if n=='+' or n=='-' or n=='*' or n=='/':
    def operations():
        if n=='+':
            inp()
            # maininp()
            print("Result Of Addition =",a+b)
        elif n=='-':
            inp()
            print("Result Of Subtraction =",a-b)
    operations()
def again():
    print("Do You Want To Use Calculator Again y/n")
again()
# maininp()
while True:
    if n == 'y':
        op()
        # maininp()
        inp()
        n = str(input())
        operations()
    elif n =='n':
        print("Thank You For Using Sangam Calculator")
        break
    else:
        print("Invalid Input Please Try Again\n")
        break