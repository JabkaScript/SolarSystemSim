import pygame


def play_background_music():
    pygame.mixer.music.load("sound/background_music.mp3")
    pygame.mixer.music.play(-1)


def play_env_sounds():
    sun_sound = pygame.mixer.Sound("sound/sun_sound.mp3")
    sun_sound.set_volume(0.2)
    sun_sound.play()
