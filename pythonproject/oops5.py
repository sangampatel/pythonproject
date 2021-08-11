class info:
    def __init__(self,name,age,work):
        self.name = name
        self.age  = age
        self.work = work
name = str(input("Enter Your Name\n"))
age  = int(input("Enter Your Age\n"))
work = str(input("Enter Your Proffesion\n"))
detail = info(name,age,work)
print(detail.name,detail.age,detail.work)
class talent:
    def __init__(self,games,music):
        self.game = games
        self.music = music
# extra  = talent("Cricket","Sitar") Static object
# print(extra.game,extra.music)
games  = str(input("Enter Your Games\n"))
music  = str(input("Enter Your Music\n"))
extra  = talent(games,music)
print(extra.game, extra.music)
class alldetail(info,talent):
    def __init__(self,loc):
        self.loc = loc
loc = str(input("Enter Your Location\n"))
ald = alldetail(loc)
print(detail.name,detail.age,detail.work,extra.game,extra.music,ald.loc)