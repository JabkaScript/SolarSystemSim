import pygame
from button import Button


class UserInterface:
    def __init__(self, WIN):
        self.WIDTH = WIN.get_width()
        self.HEIGHT = WIN.get_height() // 10
        self.WIN = WIN
        self.BG = 0
        self.button_array = []
        self.toggled = False

    def draw_background(self):
        self.BG = pygame.draw.rect(self.WIN, (53, 59, 179), (0, 0, self.WIDTH, self.HEIGHT), width=2)

    def button_init(self):
        minus_button = Button(20, 10, pygame.image.load("buttons/minus_button.png"), "timestep_dec")
        minus_button.image = pygame.transform.scale(minus_button.image, (self.HEIGHT - 20, self.HEIGHT - 20))
        minus_button.update_rect()
        self.button_array.append(minus_button)

        velocity_button = Button(minus_button.image.get_rect().topright[0] + 30, 10,
                                 pygame.image.load("buttons/velocity_field.png"),
                                 "velocity")
        velocity_button.image = pygame.transform.scale(velocity_button.image, (self.HEIGHT + 50, self.HEIGHT - 20))
        velocity_button.update_rect()
        self.button_array.append(velocity_button)

        plus_button = Button(velocity_button.rect.topright[0] + 10, 10,
                              pygame.image.load("buttons/plus_button.png"), "timestep_inc")
        plus_button.image = pygame.transform.scale(plus_button.image, (self.HEIGHT - 20, self.HEIGHT - 20))
        plus_button.update_rect()
        self.button_array.append(plus_button)
        focus_info_button = Button(self.BG.topright[0]-100, 10, pygame.image
                                   .load("buttons/info_button.png"), "focus_info")
        focus_info_button.image = pygame.transform.scale(focus_info_button.image, (self.HEIGHT - 20, self.HEIGHT - 20))
        focus_info_button.update_rect()
        self.button_array.append(focus_info_button)

    def draw_buttons(self):
        for button in self.button_array:
            button.draw(self.WIN)
