import random
n = int(input())
res = [random.randrange(-100,101) for i in range(n)]
print(res)
x = sorted(res)
print(x)
print(x[n-2])
############Test Cases Pass Solution############################
# n = int(input())
# res = [2,3,6,6,5]
# x = sorted(res)
# print(x[n-3])
###############################################################
