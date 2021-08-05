def star():
    print("How Much Rows You Want")
    n = int(input())
    print("Enter 1 or Non Zero for True and 0 For False")
    n2 = int(input())
    n1 = bool((n2))
    if n1 is True:
        for i in range(n):
            i = i+1
            print(i*"*")
    elif n1 is False:
        for i in range(n):
            i = n-i
            print(i*"*")
star()