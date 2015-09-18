__author__ = 'Mitch Powell'
from Classes import *
import random

def PopPrison(population):
    prislist = []
    prislist.append(prisoner(False,0,True))
    for pris in range(0,(population-1)):
        prislist.append(prisoner(False,0,False))
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

def run(prisoners):
    Prislist = PopPrison(prisoners)
    Switch = initialize()
    prisoncount = 0
    Selectcount = 0
    while True:
        Selected = random.randint(0,len(Prislist)-1)
        if prisoncount == (2*(prisoners-1)):
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
    total = 1
    iterations = 1000
    prisoners = 40
    for x in range(iterations):
        total += run(prisoners)
    print("Average number of prisoner selections to algorithm completion: "+str(total/iterations))

Main()
