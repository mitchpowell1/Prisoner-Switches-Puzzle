__author__ = 'Mitch Powell'
class prisoner:
    def __init__(self, visitstate, visited, leader):
        self.visitstate = visitstate
        self.visited = visited
        self.leader =  leader
class switch:
    def __init__(self, Astate, Bstate):
        self.Astate = Astate
        self.Bstate = Bstate

    def Aswitch(self):
        self.Astate = not self.Astate
    def Bswitch(self):
        self.Bstate = not self.Bstate