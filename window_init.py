import pygame
import main_screen
import math_base
from pygame.locals import *

import user_interface

pygame.init()
WIDTH = 1920
HEIGHT = 1080

SCALED = True

nameFont = pygame.font.SysFont("Comic Sans MS", 25)

user_location_x = 0
user_location_y = 0
something_clicked = False
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN, vsync=1)
pygame.display.set_caption("ABOBA")
usr_int = user_interface.UserInterface(WIN)


def start_program():
    global user_location_x
    global SCALED
    global user_location_y
    loop = True
    clock = pygame.time.Clock()
    planet_counter = 1
    orbit_in_way = False
    usr_int.button_init()
    main_screen.define_main_objects_images()
    main_screen.set_planet_scale()
    while loop:
        clock.tick(60)
        WIN.fill((0, 0, 0))
        main_screen.draw_main_objects()
        draw_UI()
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
                            SCALED = False
                            math_base.increase_scale()
                        case pygame.K_DOWN:
                            SCALED = False
                            math_base.decrease_scale()
                        case pygame.K_c:
                            math_base.clear_orbits()
                        case pygame.K_y:
                            if not orbit_in_way:
                                orbit_in_way = True
                            else:
                                orbit_in_way = False
                        case pygame.K_q:
                            if planet_counter + 1 < len(main_screen.OBJECT_ARRAY):
                                planet_counter += 1
                            else:
                                planet_counter = 1
                        case pygame.K_r:
                            if planet_counter > 1:
                                planet_counter -= 1
                            else:
                                planet_counter = len(main_screen.OBJECT_ARRAY) - 1
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
            orbit = main_screen.OBJECT_ARRAY[planet_counter].orbit
            # orbit = solar_system_stat.Moon.orbit
            if len(orbit) > 0:
                x, y = orbit[len(orbit) - 1]
                user_location_x = (x * math_base.orbit_scale) / -1
                user_location_y = (y * math_base.orbit_scale) / -1
    pygame.quit()


def draw_UI():
    usr_int.draw_background()
    usr_int.draw_buttons()
    pygame.display.update()
