import pygame

import math_base
import solar_system_stat
import window_init
from pygame.locals import *

satellite_counter = 0
orbit_in_way = False


def set_on_click_listener():
    global orbit_in_way, satellite_counter
    focus_object = window_init.focus_object
    if satellite_counter > len(focus_object.satellite_array):
        window_init.satellite_counter = 0
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                window_init.loop = False
            case pygame.MOUSEBUTTONDOWN:
                match event.button:
                    case 4:
                        window_init.SCALED = False
                        math_base.increase_scale()
                    case 5:
                        window_init.SCALED = False
                        math_base.decrease_scale()
            case pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE:
                        window_init.loop = False
                    case pygame.K_1:
                        window_init.change_focus_and_scale(solar_system_stat.Sun)
                    case pygame.K_2:
                        window_init.change_focus_and_scale(solar_system_stat.Mercury)
                    case pygame.K_3:
                        window_init.change_focus_and_scale(solar_system_stat.Venus)
                    case pygame.K_4:
                        window_init.change_focus_and_scale(solar_system_stat.Earth)
                    case pygame.K_5:
                        window_init.change_focus_and_scale(solar_system_stat.Mars)
                    case pygame.K_6:
                        window_init.change_focus_and_scale(solar_system_stat.Jupiter)
                    case pygame.K_7:
                        window_init.change_focus_and_scale(solar_system_stat.Saturn)
                    case pygame.K_8:
                        window_init.change_focus_and_scale(solar_system_stat.Uranus)
                    case pygame.K_9:
                        window_init.change_focus_and_scale(solar_system_stat.Neptune)
                    case pygame.K_UP:
                        window_init.SCALED = False
                        math_base.increase_scale()
                    case pygame.K_DOWN:
                        window_init.SCALED = False
                        math_base.decrease_scale()
                    case pygame.K_c:
                        math_base.clear_orbits(focus_object)
                    case pygame.K_y:
                        if not orbit_in_way:
                            orbit_in_way = True
                        else:
                            orbit_in_way = False
                    case pygame.K_q:
                        if satellite_counter + 1 < len(focus_object.satellite_array):
                            satellite_counter += 1
                        else:
                            satellite_counter = 0
                    case pygame.K_r:
                        if satellite_counter > 0:
                            satellite_counter -= 1
                        else:
                            satellite_counter = len(focus_object.satellite_array) - 1
                    case pygame.K_o:
                        if window_init.orbit_needed:
                            window_init.orbit_needed = False
                        else:
                            window_init.orbit_needed = True
                    case pygame.K_l:
                        print(window_init.user_location_x, window_init.user_location_y)

    if pygame.key.get_pressed()[K_w]:
        math_base.clear_scaled_orbits(focus_object)
        window_init.user_location_y += 20
    if pygame.key.get_pressed()[K_s]:
        math_base.clear_scaled_orbits(focus_object)
        window_init.user_location_y -= 20
    if pygame.key.get_pressed()[K_a]:
        math_base.clear_scaled_orbits(focus_object)
        window_init.user_location_x += 20
    if pygame.key.get_pressed()[K_d]:
        math_base.clear_scaled_orbits(focus_object)
        window_init.user_location_x -= 20
    if pygame.key.get_pressed()[K_LEFT]:
        math_base.clear_scaled_orbits(focus_object)
        math_base.clear_orbits(focus_object)
        math_base.decrease_timestep_tick()
    if pygame.key.get_pressed()[K_RIGHT]:
        math_base.clear_scaled_orbits(focus_object)
        math_base.clear_orbits(focus_object)
        math_base.increase_timestep_tick()
    if orbit_in_way and len(focus_object.satellite_array) > 0:
        window_init.SCALED = False
        window_init.track_object_in_screen(focus_object.satellite_array[satellite_counter])


