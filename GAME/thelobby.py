def lobby():
    from GAME.help import needhelp
    import pygame
    import pygame_menu
    from pygame_menu import Theme
    from GAME.main import level_the_first

    pygame.init()
    screen = pygame.display.set_mode([1248, 960])
    font = pygame.font.Font(None, 100)
    style = pygame_menu.widgets.MENUBAR_STYLE_NONE
    menu = pygame_menu.Menu('', 1248, 960,
                            theme=Theme(
                                background_color=(115, 107, 173),
                                scrollbar_slider_hover_color=(100, 96, 90),
                                selection_color=(50, 255, 0),
                                title_background_color=(50, 255, 100),
                                title_bar_style=style,
                                title_font_color=(255, 0, 255),
                                widget_font=font,
                                widget_font_color=(255, 255, 255)

                            ))

    menu.add.button("ИГРАТЬ!!!!", level_the_first)
    menu.add.button('ПОМОЩЬ', needhelp)
    menu.add.button('ВЫЙТИ', pygame_menu.events.EXIT)
    menu.add.button('В игре присутвует вспышка')
    menu.mainloop(screen)
