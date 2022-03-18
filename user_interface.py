import pygame
from button import Button


class UserInterface:
    def __init__(self, WIN):
        self.WIDTH = WIN.get_width()
        self.HEIGHT = WIN.get_height() // 10
        self.WIN = WIN
        self.button_array = []

    def draw_background(self):
        pygame.draw.rect(self.WIN, (255, 255, 255), (0, 0, self.WIDTH, self.HEIGHT))

    def button_init(self):
        plus_button = Button(20, 10, pygame.image.load("buttons/plus_button.png"), "timestep_inc")
        plus_button.image = pygame.transform.scale(plus_button.image, (self.HEIGHT-20, self.HEIGHT-20))
        plus_button.update_rect()
        self.button_array.append(plus_button)

        velocity_button = Button(plus_button.image.get_rect().topright[0]+30, 10, pygame.image.load("buttons/velocity_field.png"),
                                 "velocity")
        velocity_button.image = pygame.transform.scale(velocity_button.image, (self.HEIGHT+50, self.HEIGHT - 20))
        velocity_button.update_rect()
        self.button_array.append(velocity_button)

        minus_button = Button(velocity_button.rect.topright[0]+10, 10,
                              pygame.image.load("buttons/minus_button.png"), "timestep_dec")
        minus_button.image = pygame.transform.scale(minus_button.image, (self.HEIGHT - 20, self.HEIGHT - 20))
        velocity_button.update_rect()
        self.button_array.append(minus_button)

    def draw_buttons(self):
        for button in self.button_array:
            button.draw(self.WIN)

