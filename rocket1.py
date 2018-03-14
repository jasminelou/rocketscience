from ggrocket import Rocket, Planet

earth = Planet(viewscale=0.000005)
rocket = Rocket(earth, altitude=400000, velocity=1000, timezoom=1)
earth.run(rocket)