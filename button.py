import pygame
import math_base
import window_init


class Button():
    def __init__(self, x, y, image, type):
        self.x = x
        self.y = y
        self.image = image
        self.rect = image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.type = type

    def draw(self, win):
        win.blit(self.image, self.rect)
        if self.type == "velocity":
            timestep = math_base.timestep/3600
            metric = "л/с" if timestep>365 else "м/c" if timestep>30 else "д/с"
            timestep = timestep//365 if metric == "л/с" else timestep//30 if metric == "м/c" else timestep
            velocity = window_init.nameFont.render(str(timestep)+metric, False, (0, 0, 0))
            win.blit(velocity, (self.rect.centerx-35, self.rect.centery-20))
        self.on_click_listener()

    def on_click_listener(self):
        pos = pygame.mouse.get_pos()
        self.rect.topleft = (self.x, self.y)
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed(3)[0] == 1 and not window_init.something_clicked:
                window_init.something_clicked = True
                match self.type:
                    case "timestep_inc":
                        math_base.increase_timestep()
                    case "timestep_dec":
                        math_base.decrease_timestep()
        if pygame.mouse.get_pressed(3)[0] == 0:
            window_init.something_clicked = False


    def update_rect(self):
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
