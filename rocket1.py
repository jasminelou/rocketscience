from ggrocket import Rocket, Planet

earth = Planet(viewscale=0.000005)
rocket = Rocket(earth, altitude=2000000, velocity=6900, timezoom=1)
earth.run(rocket)