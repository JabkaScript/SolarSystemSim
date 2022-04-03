import pygame
import drawning_methods
import math_base
import events_handler
import music_handler

import solar_system_stat
import user_interface

pygame.init()
WIDTH = 1920
HEIGHT = 1080

SCALED = True

nameFont = pygame.font.SysFont("Comic Sans MS", 25)
something_clicked = False
orbit_needed = False
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN, vsync=1)
focus_object = solar_system_stat.Sun
user_location_x = (focus_object.x * math_base.orbit_scale) * -1
user_location_y = (focus_object.y * math_base.orbit_scale) * -1
usr_int = user_interface.UserInterface(WIN)
music_handler.play_background_music()
music_handler.play_env_sounds()


def start_program():
    global focus_object, loop, user_location_x, user_location_y, SCALED
    background_image = pygame.image.load("env/background.jpg")
    rect = background_image.get_rect()
    background_image = pygame.transform.scale(background_image, (WIN.get_width(), WIN.get_height()))
    loop = True
    clock = pygame.time.Clock()
    usr_int.draw_background()
    usr_int.button_init()
    drawning_methods.define_main_objects_images()
    drawning_methods.set_planet_scale()
    while loop:
        clock.tick(75)
        WIN.fill((0, 0, 0))
        WIN.blit(background_image, rect)
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
    x, y = space_object.x, space_object.y
    user_location_x = (x * math_base.orbit_scale) / -1
    user_location_y = (y * math_base.orbit_scale) / -1


def change_focus_and_scale(new_focus):
    global focus_object, SCALED
    focus_object = new_focus
    SCALED = False
    if new_focus != solar_system_stat.Sun:
        math_base.planet_scale = 100000
        math_base.orbit_scale = 1000.681818181818182e-09
    else:
        math_base.orbit_scale = 0.000000006
        math_base.planet_scale = 150000
    set_focus_in_center_of_vision(focus_object)
    if focus_object != solar_system_stat.Sun: math_base.move_satellites_to_parent(focus_object)
