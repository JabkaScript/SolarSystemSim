from space_objects import *
import pygame
import math_base

Sun = SpaceObject("Sun", 0, 0, "yellow", 1.98892 * 10 ** 30, 69599000, "star")

Mercury = SpaceObject("Mercury", 0.387 * math_base.AU, 0, "yellow", 3.30 * 10 ** 23, 2439000, "planet")
Mercury.y_velocity = -47.4 * 1000

Venus = SpaceObject("Venus", 0.723 * math_base.AU, 0, "orange", 4.87 * 10 ** 24, 6052000, "planet")
Venus.y_velocity = -35.02 * 1000

Earth = SpaceObject("Earth", math_base.AU, 0, "green", 5.97 * 10 ** 24, 6371000, "planet")
Earth.y_velocity = -29.78 * 1000

Mars = SpaceObject("Mars", 1.52 * math_base.AU, 0, "red", 6.42 * 10 ** 23, 3389000, "planet")
Mars.y_velocity = -24.13 * 1000

Jupiter = SpaceObject("Jupiter", 5.204 * math_base.AU, 0, (180, 134, 128), 1.8986 * 10 ** 27, 6991100, "planet")
Jupiter.y_velocity = -13.07 * 1000

Saturn = SpaceObject("Saturn", 9.54 * math_base.AU, 0, (230, 212, 176), 5.68 * 10 ** 26, 5823200, "planet")
Saturn.y_velocity = -9.68 * 1000

Uranus = SpaceObject("Uranus", 19.2 * math_base.AU, 0, (191, 255, 255), 8.68 * 10 ** 25, 25362000, "planet")
Uranus.y_velocity = -6.81 * 1000

Neptune = SpaceObject("Neptune", 30.1*math_base.AU, 0, (75, 112, 221), 1.02*10**26, 24662000, "planet")
Neptune.y_velocity = -5.4349*1000

#Moon = SpaceObject("Moon", Earth.x+384467*1000, 0, "gray", 7.35 * 10 ** 22, 1737000, "satellite")
#Moon.y_velocity = -1.02*1000
#Earth.satellite_array.append(Moon)
