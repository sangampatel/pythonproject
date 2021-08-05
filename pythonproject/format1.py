n = int(input())
def format():
    for i in range(n):
        y = i+1
        print(y)
    for j in range(n):
        x = j+1
        x1 = oct(x)
        print(x1)
    for k in range(n):
        z = k+1
        z1 = hex(z)
        print(z1)
    for l in range(n):
        w = l+1
        w1 = bin(w)
        print(w1)
format()

