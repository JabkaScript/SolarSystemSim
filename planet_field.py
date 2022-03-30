
import window_init
import pygame
import button


class PlanetField:
    def __init__(self, x, y, image, space_object):
        self.object_name = space_object.name
        self.image = image
        self.x = x
        self.y = y
        self.next_y = y
        self.object_link = space_object
        self.rect = image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.UI_elements_list = []

    def draw(self, win):
        pass

    def define_field_and_button(self):
        planet_name = window_init.nameFont.render(self.object_name, False, (0, 0, 0))
        planet_info_button = button.Button(self.rect.topright[0] - 10, self.y+10,
                                           self.image, "planet_info", self.object_link)
        planet_tracking_button = button.Button(self.rect.topright[0],
                                               self.y+10, self.image, "planet_tracking", self.object_link)
        self.UI_elements_list.append(planet_name)
        self.UI_elements_list.append(planet_info_button)
        self.UI_elements_list.append(planet_tracking_button)
