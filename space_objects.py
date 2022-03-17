import pygame

import math_base
import window_init


class SpaceObject:
    # Имя, начальное положение по осям oX и oY, масса , средний радиус тип объекта
    def __init__(self, name, x, y, color, mass, radius, object_type="unknown_object",):
        self.x = x
        self.y = y
        self.mass = mass
        self.name = name
        self.type = object_type
        self.radius = radius
        self.color = color
        self.satellite_array = []
        self.orbit = []
        self.scaled_orbit = []
        self.x_velocity = 0
        self.y_velocity = 0
        self.image = 0
        self.drawable_image = 0

    def draw(self, win):
        x = self.x * math_base.orbit_scale + window_init.WIDTH / 2 + window_init.user_location_x
        y = self.y * math_base.orbit_scale + window_init.HEIGHT / 2 + window_init.user_location_y
        rect = self.drawable_image.get_rect()
        rect.center = (x, y)
        planet_name = window_init.nameFont.render(self.name, False, (255, 255, 255))
        win.blit(self.drawable_image, rect)
        win.blit(planet_name, (rect.centerx-50, rect.centery))

    def draw_orbit(self, win):
        scaled_orbit = []
        orbit = self.orbit
        if len(orbit) > 2:
            for point in orbit:
                    x, y = point
                    x = x * math_base.orbit_scale + window_init.WIDTH / 2 + window_init.user_location_x
                    y = y * math_base.orbit_scale + window_init.HEIGHT / 2 + window_init.user_location_y
                    scaled_orbit.append((x, y))
            pygame.draw.lines(win, self.color, False, scaled_orbit, 2)



    def draw_satellites(self, win):
        for satellite in self.satellite_array:
            x = satellite.x * math_base.orbit_scale + window_init.WIDTH / 2 + window_init.user_location_x
            y = satellite.y * math_base.orbit_scale + window_init.HEIGHT / 2 + window_init.user_location_y
            rect = satellite.drawable_image.get_rect()
            rect.center = (x, y)
            planet_name = window_init.nameFont.render(satellite.name, False, (255, 255, 255))
            win.blit(planet_name, (rect.centerx - 50, rect.centery))
            win.blit(satellite.drawable_image, rect)
            #satellite.draw_orbit(win)


