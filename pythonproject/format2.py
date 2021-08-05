n = int(input())
def deci(n):
    #for i in range(n):
    x = n
    return x
def octl(n):
    # for i in range(n):
    #     x1 = i + 1
    y = oct(n)
    return y
def hexa(n):
    #for i in range(n):
        #x2 = i + 1
        #z = hex(x2)
    z = hex(n)
    return z
def bina(n):
    #for i in range(n):
        #x3 = i + 1
        #w = bin(x3)
    w = bin(n)
    return w
for k in range(1,n+1):
    print(deci(k),octl(k),hexa(k),bina(k))



