def level_the_second():
    from main2 import level_the_global1
    import pygame
    pygame.init()
    wall_width = 32
    wall_height = 32
    step = 10
    screen = pygame.display.set_mode([1248, 960])
    fon = pygame.image.load("texturse/fon.png")
    fon = pygame.transform.scale(fon, (1248, 960))

    font = pygame.font.Font(None, 50)
    text = font.render("-Здравствуй, внучок мой, как дела?", 1, [255, 255, 255])
    text1 = font.render("-Да я квартиру свою найти не могу и ключи потерял...", 1, [255, 255, 255])
    text2 = font.render("-Проблема... О! Я же недавно ключик в подъезде нашла! Держи",1, [255, 255, 255])
    text3 = font.render("-Спасибо, Александра Игоревна!", 1, [255, 255, 255])

    stone = pygame.image.load("texturse/мрамор итальянский.jpg")
    stone = pygame.transform.scale(stone, (wall_width, wall_height))

    babka = pygame.image.load("texturse/бабка.png")
    babka = pygame.transform.scale(babka, (160, 160))

    key = pygame.image.load("texturse/ключ.png")
    key = pygame.transform.scale(key, (32, 32))
    key_r = key.get_rect(topleft=(64, 548))

    player = pygame.image.load("texturse/персик/персик11.png")
    player = pygame.transform.scale(player, (32, 64))
    player_r = player.get_rect(topleft=(32, 512))
    walk = [pygame.transform.scale(pygame.image.load("texturse/персик/персик11.png"), (32, 64))]
    player_image_number = 0
    walk_right = [pygame.transform.scale(pygame.image.load("texturse/персик/персик41.png"), (32, 64)),
                  pygame.transform.scale(pygame.image.load("texturse/персик/персик42.png"), (32, 64)),
                  pygame.transform.scale(pygame.image.load("texturse/персик/персик43.png"), (32, 64)),
                  pygame.transform.scale(pygame.image.load("texturse/персик/персик44.png"), (32, 64))]

    walk_left = [pygame.transform.scale(pygame.image.load("texturse/персик/персик31.png"), (32, 64)),
                 pygame.transform.scale(pygame.image.load("texturse/персик/персик32.png"), (32, 64)),
                 pygame.transform.scale(pygame.image.load("texturse/персик/персик33.png"), (32, 64)),
                 pygame.transform.scale(pygame.image.load("texturse/персик/персик34.png"), (32, 64))]
    karta = ["***************************************",
             "***************************************",
             "***************************************",
             "***************************************",
             "***************************************",
             "***************************************",
             "***************************************",
             "***************************************",
             "***************************************",
             "***************************************",
             "***************************************",
             "                                       ",
             "                                       ",
             "                                       ",
             "                                       ",
             "                                       ",
             "                                       ",
             "                                       ",
             "***************************************",
             "***************************************",
             "***************************************",
             "***************************************",
             "***************************************",
             "***************************************",
             "***************************************",
             "***************************************",
             "***************************************",
             "***************************************",
             "***************************************",
             "***************************************"]
    stop = []
    running = True
    while running:
        keys = pygame.key.get_pressed()
        screen.blit(fon, (0, 0))
        x = y = 0
        for row in karta:
            for col in row:
                if col == "*":
                    bl = screen.blit(stone, (x, y))
                    stop.append(bl)
                x += wall_width
            y += wall_height
            x = 0
        screen.blit(key, key_r)
        screen.blit(walk[player_image_number // 3], player_r)
        velX = 0
        velY = 0

        if keys[pygame.K_a] or keys[pygame.K_LEFT] and player_r.x > 0:
            velX = -step
            player_image_number += 1
            walk = walk_left
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT] and player_r.x < 1216:
            velX = step
            player_image_number += 1
            walk = walk_right
        else:
            player_image_number = 0
        if player_image_number > 11:
            player_image_number = 0

        player_r.x = player_r.x + velX

        player_r.y = player_r.y + velY
        for s in stop:
            if player_r.colliderect(s):
                if velY < 0:
                    player_r.top = s.bottom
                    velY = 0
                elif velY > 0:
                    player_r.bottom = s.top
                    velY = 0

        if player_r.colliderect(key_r) and keys[pygame.K_e]:
            key_r.x = 10000
        if key_r.x != 64:
            level_the_global1()
        screen.blit(text, (100,50))
        screen.blit(text1, (100,100))
        screen.blit(text2, (100, 150))
        screen.blit(text3, (100,200))
        screen.blit(babka, (400, 416))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
    pygame.quit()