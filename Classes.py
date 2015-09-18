__author__ = 'BigBear'
class prisoner:
    def __init__(self,name, visitstate, visited, leader):
        self.name = name
        self.visitstate = visitstate
        self.visited = visited
        self.leader =  leader
class switch:
    def __init__(self, Astate, Bstate):
        self.Astate = Astate
        self.Bstate = Bstate

    def Aswitch(self):
        if self.Astate == True:
            self.Astate = False
        else:
            self.Astate = True
    def Bswitch(self):
        if self.Bstate == True:
            self.Bstate = False
        else:
            self.Bstate = True
