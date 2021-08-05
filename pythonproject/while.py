l = ["Monday","Tuesday","Wednesday",4,5,6,7,255,34,-78,78,6,91]
def whileloop(l):
    i =0
    while i<len(l):
        if str(l[i]).isnumeric() and l[i]>=6:
            print(l[i])
        i = i+1
whileloop(l)