import pygame

pygame.init()
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ABOBA")


def start_program():
    loop = True
    clock = pygame.time.Clock()

    while loop:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
    pygame.quit()
