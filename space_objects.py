import pygame
import math_base
import planet_info_window
import window_init


class SpaceObject:
    # Имя, начальное положение по осям oX и oY, масса , средний радиус тип объекта
    def __init__(self, name, x, y, color, mass, radius, object_type="unknown_object", ):
        self.x = x
        self.y = y
        self.info = ""
        self.distance_to_parent = x
        self.mass = mass
        self.name = name
        self.type = object_type
        self.radius = radius
        self.color = color
        self.first_time_orbit = True
        self.satellite_array = []
        self.x_velocity = 0
        self.y_velocity = 0
        self.original_y_velocity = 0
        self.image = 0
        self.drawable_image = 0
        self.drawable_image_rect = 0
        self.real_image = 0

    def draw(self, win):
        x = self.x * math_base.orbit_scale + window_init.WIDTH / 2 + window_init.user_location_x
        y = self.y * math_base.orbit_scale + window_init.HEIGHT / 2 + window_init.user_location_y
        rect = self.drawable_image_rect = self.drawable_image.get_rect()
        rect.center = (x, y)
        planet_name = window_init.nameFont.render(self.name, False, (255, 255, 255))
        win.blit(self.drawable_image, rect)
        win.blit(planet_name, (rect.center[0],rect.bottomleft[1]))
        self.display_info_on_click()

    def draw_orbit(self, win):
        pygame.draw.circle(win, self.color, (
            window_init.focus_object.x * math_base.orbit_scale + window_init.WIDTH / 2 + window_init.user_location_x,
            window_init.focus_object.y * math_base.orbit_scale + window_init.HEIGHT / 2 + window_init.user_location_y),
                           self.distance_to_parent * math_base.orbit_scale, 2)

    def draw_satellites(self, win):
        for satellite in self.satellite_array:
            if window_init.orbit_needed: satellite.draw_orbit(win)
            x = satellite.x * math_base.orbit_scale + window_init.WIDTH / 2 + window_init.user_location_x
            y = satellite.y * math_base.orbit_scale + window_init.HEIGHT / 2 + window_init.user_location_y
            rect = satellite.drawable_image_rect = satellite.drawable_image.get_rect()
            rect.center = (x, y)
            planet_name = window_init.nameFont.render(satellite.name, False, (255, 255, 255))
            win.blit(satellite.drawable_image, rect)
            win.blit(planet_name, (rect.center[0], rect.bottomleft[1]))
            satellite.change_focus_on_click()

    def display_info_on_click(self):
        pos = list(pygame.mouse.get_pos())
        rect = self.drawable_image_rect
        if rect.collidepoint(pos):
            if pygame.mouse.get_pressed(3)[0] == 1 and not window_init.something_clicked:
                window_init.something_clicked = True
                planet_info_window.init_and_draw(self)

    def change_focus_on_click(self):
        pos = list(pygame.mouse.get_pos())
        rect = self.drawable_image_rect
        if rect.collidepoint(pos):
            if pygame.mouse.get_pressed(3)[0] == 1 and not window_init.something_clicked:
                window_init.something_clicked = True
                window_init.change_focus_and_scale(self)
