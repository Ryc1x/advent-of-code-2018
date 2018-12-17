class Life:
    hp = 200
    atk = 3
    def __init__(self,x,y):
       self.x = x
       self.y = y

class Elf(Life):
    def __init__(self,x,y):
        Life.__init__(self,x,y)