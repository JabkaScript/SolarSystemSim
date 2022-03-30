import pygame
import drawning_methods
import math_base
import pygame_menu
from pygame.locals import *

import solar_system_stat
import user_interface

pygame.init()
WIDTH = 1920
HEIGHT = 1080

SCALED = True

nameFont = pygame.font.SysFont("Comic Sans MS", 25)
something_clicked = False
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN, vsync=1)
focus_object = solar_system_stat.Sun
user_location_x = (focus_object.x * math_base.orbit_scale) * -1
user_location_y = (focus_object.y * math_base.orbit_scale) * -1
usr_int = user_interface.UserInterface(WIN)
orbit_needed = False


def start_program():
    global focus_object
    global user_location_x
    global SCALED
    global user_location_y
    global orbit_needed
    loop = True
    clock = pygame.time.Clock()
    satellite_counter = 0
    orbit_in_way = False
    usr_int.button_init()
    drawning_methods.define_main_objects_images()
    drawning_methods.set_planet_scale()
    background_image = pygame.image.load("env/background.jpg")
    pygame.transform.scale(background_image, (WIDTH, HEIGHT))
    while loop:
        clock.tick(60)
        # WIN.blit(background_image, (0,0))
        WIN.fill((0, 0, 0))
        drawning_methods.draw_focus(focus_object)
        drawning_methods.draw_satellites(focus_object)
        drawning_methods.draw_UI(usr_int)
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    loop = False
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_ESCAPE:
                            loop = False
                            print(solar_system_stat.Sun.info)
                        case pygame.K_1:
                            math_base.clear_orbits(focus_object)
                            SCALED = False
                            focus_object = solar_system_stat.Sun
                            math_base.orbit_scale = 5.681818181818182e-09
                            math_base.planet_scale = 250000
                            set_focus_in_center_of_vision(focus_object)
                        case pygame.K_2:
                            focus_object = solar_system_stat.Mercury
                            SCALED = False
                            math_base.planet_scale = 30000
                            math_base.orbit_scale = 1000.681818181818182e-09
                            set_focus_in_center_of_vision(focus_object)
                        case pygame.K_3:
                            focus_object = solar_system_stat.Venus
                            SCALED = False
                            math_base.planet_scale = 30000
                            math_base.orbit_scale = 1000.681818181818182e-09
                            set_focus_in_center_of_vision(focus_object)
                        case pygame.K_4:
                            focus_object = solar_system_stat.Earth
                            SCALED = False
                            math_base.planet_scale = 30000
                            math_base.orbit_scale = 1000.681818181818182e-09
                            set_focus_in_center_of_vision(focus_object)
                            math_base.move_satellites_to_parent(focus_object)
                        case pygame.K_5:
                            focus_object = solar_system_stat.Mars
                            SCALED = False
                            math_base.planet_scale = 30000
                            math_base.orbit_scale = 10.681818181818182e-09
                            set_focus_in_center_of_vision(focus_object)
                            math_base.move_satellites_to_parent(focus_object)
                        case pygame.K_6:
                            focus_object = solar_system_stat.Jupiter
                            SCALED = False
                            math_base.planet_scale = 120000
                            math_base.orbit_scale = 1000.681818181818182e-09
                            set_focus_in_center_of_vision(focus_object)
                        case pygame.K_RIGHT:
                            math_base.increase_timestep()
                        case pygame.K_LEFT:
                            math_base.decrease_timestep()
                        case pygame.K_UP:
                            SCALED = False
                            math_base.increase_scale()
                        case pygame.K_DOWN:
                            SCALED = False
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
                            if satellite_counter > 1:
                                satellite_counter -= 1
                            else:
                                satellite_counter = len(focus_object.satellite_array) - 1
                        case pygame.K_o:
                            if orbit_needed:
                                orbit_needed = False
                            else:
                                orbit_needed = True
        if pygame.key.get_pressed()[K_w]:
            SCALED = False
            user_location_y += 20
        if pygame.key.get_pressed()[K_s]:
            SCALED = False
            user_location_y -= 20
        if pygame.key.get_pressed()[K_a]:
            SCALED = False
            user_location_x += 20
        if pygame.key.get_pressed()[K_d]:
            SCALED = False
            user_location_x -= 20
        if orbit_in_way:
            track_object_in_screen(focus_object.satellite_array[satellite_counter])
        pygame.display.update()
    pygame.quit()


def set_focus_in_center_of_vision(focus_object):
    global user_location_x, user_location_y
    user_location_x = (focus_object.x * math_base.orbit_scale) / -1
    user_location_y = (focus_object.y * math_base.orbit_scale) / -1


def track_object_in_screen(space_object):
    global user_location_x, user_location_y
    orbit = space_object.orbit
    if len(orbit) > 0:
        x, y = orbit[len(orbit) - 1]
        user_location_x = (x * math_base.orbit_scale) / -1
        user_location_y = (y * math_base.orbit_scale) / -1
