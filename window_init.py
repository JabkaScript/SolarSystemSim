import pygame
import main_screen
import math_base

pygame.init()
WIDTH = 1920
HEIGHT = 1080

user_location_x = 0
user_location_y = 0

WIN = pygame.display.set_mode((WIDTH, HEIGHT),pygame.FULLSCREEN)
pygame.display.set_caption("ABOBA")


def start_program():
    global user_location_x
    global user_location_y
    loop = True
    clock = pygame.time.Clock()
    while loop:
        clock.tick(120)
        WIN.fill((0,0,0))
        main_screen.draw_main_objects()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop = False
                if event.key == pygame.K_w:
                    user_location_y += 50
                if event.key == pygame.K_s:
                    user_location_y -= 50
                if event.key == pygame.K_a:
                    user_location_x += 50
                if event.key == pygame.K_d:
                    user_location_x -= 50
                if event.key == pygame.K_RIGHT:
                    math_base.increase_timestep()
                if event.key == pygame.K_LEFT:
                    math_base.decrease_timestep()
                if event.key == pygame.K_UP:
                    math_base.increase_scale()
                if event.key == pygame.K_DOWN:
                    math_base.decrease_scale()
                if event.key == pygame.K_c:
                    math_base.clear_orbits(main_screen.OBJECT_ARRAY)
    pygame.quit()
