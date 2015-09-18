__author__ = 'BigBear'
from Classes import *
import random

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
        self.Astate = not self.Astate
    def Bswitch(self):
        self.Bstate = not self.Bstate

def PopPrison():
    a = prisoner('a',False,0,True)
    b = prisoner('b',False,0,False)
    c = prisoner('c',False,0,False)
    d = prisoner('d',False,0,False)
    e = prisoner('e',False,0,False)
    f = prisoner('f',False,0,False)
    g = prisoner('g',False,0,False)
    h = prisoner('h',False,0,False)
    i = prisoner('i',False,0,False)
    j = prisoner('j',False,0,False)
    k = prisoner('k',False,0,False)
    l = prisoner('l',False,0,False)
    m = prisoner('m',False,0,False)
    n = prisoner('n',False,0,False)
    o = prisoner('o',False,0,False)
    p = prisoner('p',False,0,False)
    q = prisoner('q',False,0,False)
    r = prisoner('r',False,0,False)
    s = prisoner('s',False,0,False)
    t = prisoner('t',False,0,False)
    u = prisoner('u',False,0,False)
    v = prisoner('v',False,0,False)
    w = prisoner('w',False,0,False)
    prislist = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w]
    return(prislist)

def initialize():
    state = random.randint(1,4)
    if state == 1:
        Switch = switch(True,True)
    elif state == 2:
        Switch = switch(True,False)
    elif state == 3:
        Switch = switch(False,True)
    else:
        Switch = switch(False,False)
    return(Switch)

def run():
    Prislist = PopPrison()
    Switch = initialize()
    prisoncount = 0
    Selectcount = 0
    while True:
        Selected = random.randint(0,22)
        if prisoncount == 44:
            break
        elif Prislist[Selected].leader == True:         #if the leader is selected
            if Switch.Astate == True:                   #and the left switch is up
                prisoncount += 1                        #add one to the count
                Switch.Aswitch()                        #and flip the switch back down
        else:                                           #if someone other than the leader is selected
            if Prislist[Selected].visited < 2:          #and they have not visited before
                if Switch.Astate == False:              #and the switch is down,
                    Switch.Aswitch()                    #flip the switch up
                    Prislist[Selected].visited += 1     #and change visited state to true
            else:                                       #if the prisoner has visited more than 2 times
                Switch.Bswitch()                        #flip the dummy
        Selectcount+= 1
    return(Selectcount)

def Main():
    total = 0
    iterations = 5000
    for x in range(iterations):
        total += run()
    print("Average number of selections to algorithm completion: "+str(total/iterations))
Main()