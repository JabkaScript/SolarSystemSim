from solar_system_stat import *
import window_init
import math_base

OBJECT_ARRAY = [Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn]


def draw_main_objects():
    for object in OBJECT_ARRAY:
        math_base.calculate_next_position(object, OBJECT_ARRAY)
        math_base.calculate_next_position_for_satellites(object)
        object.draw_orbit(window_init.WIN)
        object.draw(window_init.WIN)
        object.draw_satellites(window_init.WIN)
    pygame.display.update()
