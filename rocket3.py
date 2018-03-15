from ggrocket import *
from math import *
from ggmath import *

earth = Planet(planetmass=0)

RocketStarted = False
StartTime = None
BurnTime = 0

me = 25600
mp = 395700
F1D = 716000
NID = 9
Ftotal = F1D * N1D
tburn = 180

vmax = Ftotal*tburn/(me+mp)
print("Predicted final velocity (Newton's 2nd Law), vmax: ", vmax, " m/s")

def GetThrust():
    global BurnTurn, RocketStarted
    if RocketStarted:
        BurnTime = rocket.shiptime - StartTime
        if BurnTime >= tburn:
            RocketStarted = False
            return 0
        return Ftotal
    return 0
    
def StartRocket():
    global RocketStarted