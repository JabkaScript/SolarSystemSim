from space_objects import *
import math_base
import solar_system_object_information_ru

Sun = SpaceObject("Солнце", 5000000000, 0, "yellow", 1.98892 * 10 ** 30, 69599000, "Звезда")
Sun.info = solar_system_object_information_ru.sun_info
Sun.real_image = "planets/sun_R.jpg"

Mercury = SpaceObject("Меркурий", 0.387 * math_base.AU, 0, "yellow", 3.30 * 10 ** 23, 2439000, "Планета")
Mercury.y_velocity = -47.4 * 1000
Mercury.info = solar_system_object_information_ru.mercury_info
Mercury.real_image = "planets/mercury_R.jpg"

Venus = SpaceObject("Венера", 0.723 * math_base.AU, 0, "orange", 4.87 * 10 ** 24, 6052000, "Планета")
Venus.y_velocity = -35.02 * 1000
Venus.info = solar_system_object_information_ru.venus_info
Venus.real_image = "planets/venus_R.jpg"


Earth = SpaceObject("Земля", math_base.AU, 0, "green", 5.97 * 10 ** 24, 6371000, "Планета")
Earth.y_velocity = -29.78 * 1000
Earth.info = solar_system_object_information_ru.earth_info
Earth.real_image = "planets/earth_R.jpg"

Mars = SpaceObject("Марс", 1.52 * math_base.AU, 0, "red", 6.42 * 10 ** 24, 3389000, "Планета")
Mars.y_velocity = -24.13 * 1000
Mars.info = solar_system_object_information_ru.mars_info
Mars.real_image = "planets/mars_R.jpg"

Jupiter = SpaceObject("Юпитер", 5.204 * math_base.AU, 0, (180, 134, 128), 1.8986 * 10 ** 27, 69911000, "Планета")
Jupiter.y_velocity = -13.07 * 1000
Jupiter.info = solar_system_object_information_ru.jupiter_info
Jupiter.real_image = "planets/jupiter_R.jpg"

Saturn = SpaceObject("Сатурн", 9.54 * math_base.AU, 0, (230, 212, 176), 5.68 * 10 ** 26, 58232000, "Планета")
Saturn.y_velocity = -9.68 * 1000
Saturn.info = solar_system_object_information_ru.saturn_info
Saturn.real_image = "planets/saturn_R.jpg"

Uranus = SpaceObject("Уран", 19.2 * math_base.AU, 0, (191, 255, 255), 8.68 * 10 ** 25, 25362000, "Планета")
Uranus.y_velocity = -6.81 * 1000
Uranus.info = solar_system_object_information_ru.uranus_info

Neptune = SpaceObject("Нептун", 30.1*math_base.AU, 0, (75, 112, 221), 1.02*10**26, 24662000, "Планета")
Neptune.y_velocity = -5.4349*1000
Neptune.info = solar_system_object_information_ru.neptune_info

Moon = SpaceObject("Луна", 384467*1000, 0, "gray", 7.35 * 10 ** 22, 1737000, "Спутник")
Moon.y_velocity = -1.02*1000
Moon.original_y_velocity = -1.02*1000
Earth.satellite_array.append(Moon)

Phobos = SpaceObject("Фобос", 94000*1000, 0, "gray", 1.072*16, 1100000, "Спутник")
Phobos.y_velocity = -1.02*1000
Phobos.original_y_velocity = -1.02*1000
Mars.satellite_array.append(Phobos)

Sun.satellite_array = [Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune]
OBJECT_ARRAY = [Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune]
