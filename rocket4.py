from ggrocket import *
from math import *
from ggmath import *

earth=Planet(planetmass=0)

Stage1Started = False
Stage2Started = False
PayloadLaunched = False
StartTime = None
Burntime = 0

me1 = 25600
mp1 = 395700
Ftotal1 = 6.444e6
tburn1 = 180

me2 = 3900
mp2 = 92670
Ftotal2 = 8.01e5
tburn2 = 372

mep = 13150

vmax1 = Ftotal1*tburn1/mp1*log((me1+mp1+me2+mp2+mep)/(me1+me2+mp2+mep))
vmax2 = Ftotal2*tburn2/mp2*log((me2+mp2+mep)/(mp2+mep))

print("Predicted final staged rocket velocity (Rocket Equation), vmax: ", vmax1+vmax2, " m/s")

def GetThrust():
    global StartTime, BurnTime, Stage1Started, Stage2Started, PayloadLaunched
    if Stage1Started:
        tburn = tburn1
        Ftotal = Ftotal1
    elif Stage2Started:
        tburn = tburn2
        Ftotal = Ftotal2
    if Stage1Started or Stage2Started:
        BurnTime = rocket.shiptime - StartTime
        if BurnTime >= tburn:
            if Stage1Started:
                Stage1Started = False
                Stage2Started = True
                StartTime = rocket.shiptime
                return Ftotal2
            else:
                Stage2Started = Flase
                PayloadLaunched = True
                return 0
        else:
            return Ftotal
    else:
        return 0
        
def StartRocket():
    global Stage1Started, StartTime
    if not (Stage1Started or Stage2Started):
        Stage1Started = True
        StartTime = rocket.shiptime
        
def GetMass():
    global Stage1Started, Stage2Started, PayloadLaunched
    if Stage1Started:
        return me1 + me2 + mep + mp2 + mp1*(tburn1-BurnTime)/tburn1
    elif Stage2Started:
        return me2 + mep + mp2*(tburn2-BurnTime)/tburn2
    elif PayloadLaunched:
        return mep
    else:
        return me1 + me2 + mep + mp2 + mp1
        
def GetStatus():
    global Stage1Started, Stage2Started, PayloadLaunched
    if Stage1Started:
        return "STAGE 1 FIRING"
    elif Stage2Started:
        return "STAGE 2 FIRING"
    elif PayloadLaunched:
        return "PAYLOAD DELIVERED"
    else:
        return "WAITING FOR LAUNCH"
        
start = InputButton((10,400), "START", StartRocket, positioning="physical", size=15)

status = Label((10,420), GetStatus, positioning="physical", size=15)

tz = Slider((10, 360), 0, 5, 0, positioning="physical")

rocket = Rocket(earth, thrust = GetThrust, mass = GetMass, timezoom = tz)
earth.run(rocket)