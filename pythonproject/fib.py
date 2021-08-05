def fib():
    n1 = 0
    n2 = 1
    print("Enter Input How Much Fibonacci Series You Want")
    n = int(input())
    for i in range(n):
        if i < 3:
            print(n1)
            n1 = n2
        else:
            x = n1+n2
            n1 = n2
            n2 = x
            print(x)
fib()

