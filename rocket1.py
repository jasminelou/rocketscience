from ggrocket import Rocket, Planet

earth = Planet(viewscale=5)
rocket = Rocket(earth, altitude=50)
earth.run(rocket)