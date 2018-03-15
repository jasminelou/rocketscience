from ggrocket import *
from math import *
from ggmath import *

earth = Planet(planetmass=0, viewscale=0.00005)

RocketStarted = False
StartTime = None
BurnTime = 0

me = 25600
mp = 395700
F1D = 716000
N1D = 9
Ftotal = F1D * N1D
tburn = 180

vmaxre = Ftotal*tburn/mp*log((me+mp)/me)
print("Predicted final velocity (Rocket Equation), vmax: ", vmaxre, " m/s")

def GetThrust():
    global BurnTime, RocketStarted
    if RocketStarted:
        BurnTime = rocket.shiptime - StartTime
        if BurnTime >= tburn:
            RocketStarted = False
            return 0
        return Ftotal
    return 0
    
def StartRocket():
    global RocketStarted, StartTime
    if not RocketStarted:
        RocketStarted = True
        StartTime = rocket.shiptime
        
def GetMass():
    global RocketStarted
    if RocketStarted:
        return me+ mp*(tburn-BurnTime)/tburn
    return me + mp
        
start = InputButton((10, 400), "START", StartRocket, positioning="physical", size=15)

rocket = Rocket(earth, thrust=GetThrust, mass=GetMass)
earth.run(rocket)