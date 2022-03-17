import pygame
import window_init


class UserInterface:
    def __init__(self):
        self.WIDTH = window_init.WIDTH
        self.HEIGHT = window_init.HEIGHT // 10

    def draw_background(self):
        pygame.draw.rect(window_init.WIN, (255, 255, 255), (0, 0, self.WIDTH, self.HEIGHT))
