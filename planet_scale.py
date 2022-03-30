import pygame
import window_init
from window_init import WIN
import solar_system_stat
import math_base
from drawning_methods import set_planet_scale
from pygame.locals import *


def resize_and_draw(focus_object):
    loop = True
    x, y = focus_object.orbit[len(focus_object.orbit) - 1]
    user_location_x = (x * math_base.orbit_scale) / -1
    user_location_y = (y * math_base.orbit_scale) / -1
    clock = pygame.time.Clock()
    set_planet_and_orbit_scale()
    orbit_in_way = False
    window_init.SCALED = False
    satellite_counter = 0
    while loop:
        clock.tick(60)
        WIN.fill((0, 0, 0))
        draw_focus(focus_object)
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    loop = False
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_ESCAPE:
                            loop = False
                        case pygame.K_RIGHT:
                            math_base.increase_timestep()
                        case pygame.K_LEFT:
                            math_base.decrease_timestep()
                        case pygame.K_UP:
                            window_init.SCALED = False
                            math_base.increase_scale()
                        case pygame.K_DOWN:
                            window_init.SCALED = False
                            math_base.decrease_scale()
                        case pygame.K_c:
                            math_base.clear_orbits(fo)
                        case pygame.K_y:
                            if not orbit_in_way:
                                orbit_in_way = True
                            else:
                                orbit_in_way = False
                        case pygame.K_q:
                            if satellite_counter + 1 < len(focus_object.satellite_array):
                                satellite_counter += 1
                            else:
                                satellite_counter = 1
                        case pygame.K_r:
                            if satellite_counter > 1:
                                satellite_counter -= 1
                            else:
                                satellite_counter = len(focus_object.satellite_array) - 1
        if pygame.key.get_pressed()[K_w]:
            window_init.SCALED = False
            user_location_y += 20
        if pygame.key.get_pressed()[K_s]:
            window_init.SCALED = False
            user_location_y -= 20
        if pygame.key.get_pressed()[K_a]:
            window_init.SCALED = False
            user_location_x += 20
        if pygame.key.get_pressed()[K_d]:
            window_init.SCALED = False
            user_location_x -= 20
        if orbit_in_way:
            orbit = focus_object.satellite_array[satellite_counter].orbit
            if len(orbit) > 0:
                x, y = orbit[len(orbit) - 1]
                user_location_x = (x * math_base.orbit_scale) / -1
                user_location_y = (y * math_base.orbit_scale) / -1
        pygame.display.update()
    pygame.quit()


def set_planet_and_orbit_scale():
    math_base.orbit_scale = 5.681818181818182e-09
    math_base.planet_scale = 150000


def draw_focus(object):
    math_base.calculate_next_position(object)
    if not window_init.SCALED:
        set_planet_scale()
        window_init.SCALED = True
    object.draw_orbit(window_init.WIN)
    object.draw(window_init.WIN)


