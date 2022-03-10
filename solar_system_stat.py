from space_objects import *
import math_base

Sun = SpaceObject("Sun", 0, 0,"yellow", 1.98892 * 10 ** 30, 695990, "star")

Mercury = SpaceObject("Mercury", 0.387 * math_base.AU, 0,"gray", 3.30 * 10**23, 24400, "planet")
Mercury.y_velocity = -47.4*1000

Venus = SpaceObject("Venus", 0.723*math_base.AU, 0, "orange", 4.87*10**24, 60520, "planet")
Venus.y_velocity = -35.02*1000

Earth = SpaceObject("Earth", math_base.AU, 0, "blue", 5.97*10**24, 63710, "planet")
Earth.y_velocity = -29.78*1000

Mars = SpaceObject("Mars", 1.52*math_base.AU, 0, "red", 6.42*10**23, 33890, "planet")
Mars.y_velocity = -24.13*1000

Jupiter = SpaceObject("Jupiter", 5.204*math_base.AU, 0, "orange", 1.8986*10**27, 69911, "planet")
Jupiter.y_velocity = -13.07*1000

Saturn = SpaceObject("Saturn", 9.54*math_base.AU, 0, (230,212,176), 5.68*10**26, 25, "planet")
Saturn.y_velocity = -9.68*1000

#Uranus = SpaceObject("Uranus", 2875, 2875, 14.5, "planet")

#Neptune = SpaceObject("Neptune", 4550, 4550, 17.147, "planet")

#Moon = SpaceObject("Moon", 0.002567*math_base.AU, 0, "gray", 7.35*10**22, 6, Earth, "satellite")
#Moon.y_velocity=-1*10000
#Earth.satellite_array.append(Moon)