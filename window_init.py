import pygame
import drawning_methods
import math_base
from pygame.locals import *
import events_handler

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


def start_program():
    global focus_object, loop, user_location_x, user_location_y, SCALED
    loop = True
    clock = pygame.time.Clock()
    usr_int.button_init()
    drawning_methods.define_main_objects_images()
    drawning_methods.set_planet_scale()
    background_image = pygame.image.load("env/background.jpg")
    pygame.transform.scale(background_image, (WIDTH, HEIGHT))
    while loop:
        clock.tick(75)
        WIN.fill((0, 0, 0))
        drawning_methods.draw_focus(focus_object)
        drawning_methods.draw_satellites(focus_object)
        drawning_methods.draw_UI(usr_int)
        events_handler.set_on_click_listener()
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
