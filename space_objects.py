import pygame.draw

import math_base
import window_init


class SpaceObject:
    # Имя, начальное положение по осям oX и oY, масса , средний радиус тип объекта
    def __init__(self, name, x, y, color, mass, radius, parent, object_type="unknown_object",):
        self.x = x
        self.y = y
        self.mass = mass
        self.name = name
        self.type = object_type
        self.original_radius = radius
        self.radius = radius*math_base.planet_scale
        self.color = color

        self.satellite_array = []
        self.orbit = []
        self.orbit_done = False
        self.parent = parent

        self.x_velocity = 0
        self.y_velocity = 0

    def draw(self, win):
        x = self.x * math_base.orbit_scale + window_init.WIDTH / 2 + window_init.user_location_x
        y = self.y * math_base.orbit_scale + window_init.HEIGHT / 2 + window_init.user_location_y
        pygame.draw.circle(win, self.color, (x, y), self.radius)

    def draw_orbit(self, win):
        scaled_points = []
        if len(self.orbit) >= 2:
            for point in self.orbit:
                x, y = point
                x = x * math_base.orbit_scale + window_init.WIDTH / 2 + window_init.user_location_x
                y = y * math_base.orbit_scale + window_init.HEIGHT / 2 + window_init.user_location_y
                scaled_points.append((x, y))
            pygame.draw.lines(win, "white", False, scaled_points, 1)

    def draw_satellites(self,win):
        for satellite in self.satellite_array:
            x = (satellite.x + self.x) * math_base.orbit_scale + window_init.WIDTH / 2 + window_init.user_location_x
            y = (satellite.y + self.y) * math_base.orbit_scale + window_init.HEIGHT / 2 + window_init.user_location_y
            pygame.draw.circle(win, satellite.color, (x, y), satellite.radius)
            satellite.draw_orbit(win)


