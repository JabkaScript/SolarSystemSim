import pygame.display

import custom_themes
import window_init
import pygame_menu


def init_and_draw(focus_object):
    menu = pygame_menu.Menu(focus_object.name, window_init.WIDTH, window_init.HEIGHT,
                            theme=custom_themes.planet_info_theme)
    menu.add.image(focus_object.real_image)
    menu.add.button(("Статус: " + focus_object.type))
    menu.add.button(("Год открытия: " + focus_object.info[0:4]))
    menu.add.button(("Радиус объекта (км): " + str(int(focus_object.info[7:13].replace('0','')))))
    menu.add.button(("Масса объекта (кг): " + str(focus_object.mass)))
    menu.add.button(("Количество спутников: " + str(int(focus_object.info[4:6]))))
    menu.add.button("Назад", window_init.start_program)
    menu.mainloop(window_init.WIN)
