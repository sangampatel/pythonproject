print("1-Open Account     2-Bank Operation")
n = input()
if n=='1':
    def openaccount():
        print("Open Your Account in Sangam Bank Type Your Account Number")
        account = int(input())
        print("Your Account Number is =", account)
    openaccount()
elif n=='2':
    def bankoperation():
        print("1-Cash Withdraw      2-Cash Deposit\n3-Set Pin            4-Check Balance")
        n = (input())
        if n == '1':
            def cashwithdraw():
                print("How Much Money You Want To Withdraw")
                n1 = int(input())
                print(n1, "₹ Rupees Has Been Deducted From your Account")
            cashwithdraw()
        elif n == '2':
            def cashdeposit():
                print("How Much Money You Want To Deposit")
                n1 = int(input())
                print(n1, "₹ Rupees Has Been Added in your Account")
            cashdeposit()
        elif n == '3':
            def setpin():
                print("Set Your Pin No")
                n1 = int(input())
                print("Your Pin No is =", n1)
            setpin()
        elif n == '4':
            def checkbalance():
                print("Total Balance =1000000000000000000₹")
            checkbalance()
    bankoperation()





