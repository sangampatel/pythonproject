#Making Class
class inspector:
    #Making Constructor
    def __init__(self,n,m,k):
        self.name = n
        self.age  = m
        self.size = k
inp = inspector("me",20,6.1)
print(inp.name,inp.age,inp.size)

