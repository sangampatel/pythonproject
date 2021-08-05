######Faulty Calculations(56+9=77,70-10=50,45*3=555,56/6=4)#############################################################
print("Enter What Operation You Want = +,-,*,/")
n = str(input())
# if n!='+'or n!='-' or n!='*' or n!='/':
#     print("Invalid Input Try Again")
#     exit()
print("Enter Two Numbers")
n1 = float(input())
n2 = float(input())
if n=='+':
    def sum(n1,n2):
        if n1==56 and n2==9:
            print("Sum Of Two Numbers =",77)
        else:
            print("Sum Of Two Numbers =",n1+n2)
    sum(n1,n2)
elif n=='-':
    def sub(n1,n2):
        if n1==70 and n2==10:
            print("Substraction Of Two Numbers =",50)
        else:
            print("Substraction Of Two Numbers =",n1-n2)
    sub(n1,n2)
elif n=='*':
    def mult(n1,n2):
        if n1==45 and n2==3:
            print("Multiplication Of Two Numbers =",555)
        else:
            print("Multiplication Of Two Numbers =",n1*n2)
    mult(n1,n2)
elif n=='/':
    def div(n1,n2):
        if n1==56 and n2==6:
            print("Division Of Two Numbers =",4)
        elif n2==0:
            print("Divison Of Two Numers =","Infinite")
        else:
            print("Divison Of Two Numbers =",n1/n2)
    div(n1,n2)









