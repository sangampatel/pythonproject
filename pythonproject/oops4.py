class students:
    def __init__(self,nam,id):
        self.name = nam
        self.id   = id
nam = str(input("Enter Your Name\n"))
id = int(input("Enter Your  ID\n"))
y = students(nam,id)
print(y.name,y.id)
##########Inheritence#####################
class more(students):
    def __init__(self, no):
        self.numb = no
no  = int(input("Enter Your Mobile Number\n"))
z = more(no)
print("Updated Information Of Student =",y.name,y.id,z.numb)