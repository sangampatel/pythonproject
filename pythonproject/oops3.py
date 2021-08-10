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
no  = more(549)
print(y.name,y.id,no.numb)

########################Helping Code###############################################################################################################
# class StackOverflowUser:
#     def __init__(self, name, userid, rep):
#         self.name = name
#         self.userid = userid
#         self.rep = rep
#
#
# name = input("Enter name: ")
# userid = int(input("Enter user id: "))
# rep = int(input("Enter rep: "))
#
# dave = StackOverflowUser(name, userid, rep)