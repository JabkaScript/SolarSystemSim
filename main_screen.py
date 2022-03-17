from solar_system_stat import *
import window_init
import math_base



OBJECT_ARRAY = [Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune]


# TODO("MOON PLS MY FRIEND, MOON")


def draw_main_objects():
    for object in OBJECT_ARRAY:
        math_base.calculate_next_position(object)
        math_base.calculate_next_position_for_satellites(object)
        if not window_init.SCALED:
            set_planet_scale()
            window_init.SCALED = True
        object.draw_orbit(window_init.WIN)
        object.draw(window_init.WIN)
        object.draw_satellites(window_init.WIN)
    pygame.display.update()


def define_main_objects_images():
    Sun.image = pygame.image.load("planets/sun.png")
    Mercury.image = pygame.image.load("planets/mercury.png")
    Venus.image = pygame.image.load("planets/venus.png")
    Earth.image = pygame.image.load("planets/earth.png")
    Mars.image = pygame.image.load("planets/mars.png")
    Jupiter.image = pygame.image.load("planets/jupiter.png")
    Saturn.image = pygame.image.load("planets/saturn.png")
    Uranus.image = pygame.image.load("planets/uranus.png")
    Neptune.image = pygame.image.load("planets/neptune.png")

    #Moon.image = pygame.image.load("planets/mercury.png")


def set_planet_scale():
    Sun.drawable_image = pygame.transform.scale(Sun.image, (Sun.radius // math_base.planet_scale,
                                                   Sun.radius // math_base.planet_scale))
    Mercury.drawable_image = pygame.transform.scale(Mercury.image, (Mercury.radius // math_base.planet_scale,
                                                           Mercury.radius // math_base.planet_scale))
    Venus.drawable_image = pygame.transform.scale(Venus.image, (Venus.radius // math_base.planet_scale,
                                                       Venus.radius // math_base.planet_scale))
    Earth.drawable_image = pygame.transform.scale(Earth.image, (Earth.radius // math_base.planet_scale,
                                                       Earth.radius // math_base.planet_scale))
    Mars.drawable_image = pygame.transform.scale(Mars.image, (Mars.radius // math_base.planet_scale,
                                                     Mars.radius // math_base.planet_scale))
    Jupiter.drawable_image = pygame.transform.scale(Jupiter.image, (Jupiter.radius // math_base.planet_scale,
                                                           Jupiter.radius // math_base.planet_scale))
    Saturn.drawable_image = pygame.transform.scale(Saturn.image, (Saturn.radius // math_base.planet_scale,
                                                         Saturn.radius // math_base.planet_scale))
    Uranus.drawable_image = pygame.transform.scale(Uranus.image, (Uranus.radius // math_base.planet_scale,
                                                         Uranus.radius // math_base.planet_scale))
    Neptune.drawable_image = pygame.transform.scale(Neptune.image, (Neptune.radius // math_base.planet_scale,
                                                           Neptune.radius // math_base.planet_scale))
    #Moon.drawable_image = pygame.transform.scale(Moon.image, (Moon.radius // math_base.planet_scale,
                                                                    #Moon.radius // math_base.planet_scale))
