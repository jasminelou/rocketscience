from ggrocket import *
from ggmath import *
from math import *

def calc(r, m):
    global G
    return sqrt(2*m*G/r)

re = 6.371e6
me = 5.972e24
G = 6.674e-11

Ve = calc(re,me)
print("Predicted escape velocity is " + str(Ve) + " m/s.")

tz = Slider((10, 400), 0, 5, 0, positioning="physical")

earth = Planet()
rocket = Rocket(earth, heading=radians(90), directiond=90, velocity=Ve, timezoom=tz)
earth.run(rocket)