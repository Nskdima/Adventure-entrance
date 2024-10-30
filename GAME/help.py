def needhelp():
    import pygame
    from GAME.thelobby import lobby
    pygame.init()
    screen = pygame.display.set_mode([1248, 960])
    fon = pygame.image.load("GAME/texturse/fonforhelp.jpg")
    fon = pygame.transform.scale(fon, (1248, 960))
    font = pygame.font.Font(None, 100)
    text = font.render("Привет, друг, я разработчик этой", 1, [255, 255, 255])
    text2 = font.render("игры! Не знаю где ты её скачал,но", 1, [255, 255, 255])
    text3 = font.render("ладно ходить w a s d, стрелки.", 1, [255, 255, 255])
    text4 = font.render('Открыть дверь E. Чтобы вернуться', 1, [255, 255, 255])
    text5 = font.render(" в лобби нажми Enter.", 1, [255, 255, 255])
    running = True
    while running:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_KP_ENTER]:
            lobby()
        screen.blit(fon, (0, 0))
        screen.blit(text, (0, 0))
        screen.blit(text2, (0, 100))
        screen.blit(text3, (0, 200))
        screen.blit(text4, (0, 300))
        screen.blit(text5, (0, 400))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
    pygame.quit()
