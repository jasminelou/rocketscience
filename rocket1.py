from ggrocket import Rocket, Planet

earth = Planet(viewscale=0.000005, color=0x800080)
rocket = Rocket(earth, altitude=2000000, velocity=6900.39, timezoom=3)
earth.run(rocket)