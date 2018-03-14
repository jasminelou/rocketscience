from ggrocket import *
from math import *

earth = Planet()
rocket = Rocket(earth, heading=radians(90), directiond=90, velocity=20)
earth.run(rocket)