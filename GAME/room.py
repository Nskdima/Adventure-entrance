def level_the_room():
    import pygame
    from GAME.thelobby import lobby
    pygame.init()
    wall_width = 32
    wall_height = 32
    step = 10
    font = pygame.font.Font(None, 100)
    text = font.render("Ты прошёл игру, молодец!", 1, [255, 255, 255])
    text1 = font.render("Нажми кнопку Enter,", 1, [255, 255, 255])
    text2 = font.render("чтобы попасть в главное меню!!", 1, [255, 255, 255])
    screen = pygame.display.set_mode([1248, 960])
    fon = pygame.image.load("GAME/texturse/fon.png")
    fon = pygame.transform.scale(fon, (1248, 960))
    stone = pygame.image.load("GAME/texturse/мрамор итальянский.jpg")
    stone = pygame.transform.scale(stone, (wall_width, wall_height))

    player = pygame.image.load("GAME/texturse/персик/персик11.png")
    player = pygame.transform.scale(player, (32, 64))
    player_r = player.get_rect(topleft=(32, 512))
    walk = [pygame.transform.scale(pygame.image.load("GAME/texturse/персик/персик11.png"), (32, 64))]
    player_image_number = 0
    walk_right = [pygame.transform.scale(pygame.image.load("GAME/texturse/персик/персик41.png"), (32, 64)),
                  pygame.transform.scale(pygame.image.load("GAME/texturse/персик/персик42.png"), (32, 64)),
                  pygame.transform.scale(pygame.image.load("GAME/texturse/персик/персик43.png"), (32, 64)),
                  pygame.transform.scale(pygame.image.load("GAME/texturse/персик/персик44.png"), (32, 64))]

    walk_left = [pygame.transform.scale(pygame.image.load("GAME/texturse/персик/персик31.png"), (32, 64)),
                 pygame.transform.scale(pygame.image.load("GAME/texturse/персик/персик32.png"), (32, 64)),
                 pygame.transform.scale(pygame.image.load("GAME/texturse/персик/персик33.png"), (32, 64)),
                 pygame.transform.scale(pygame.image.load("GAME/texturse/персик/персик34.png"), (32, 64))]
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
             "*                                     *",
             "*                                     *",
             "*                                     *",
             "*                                     *",
             "*                                     *",
             "*                                     *",
             "*                                     *",
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

        if keys[pygame.K_KP_ENTER]:
            lobby()

        for s in stop:
            if player_r.colliderect(s):
                if velX < 0:
                    player_r.left = s.right
                    velX = 0
                elif velX > 0:
                    player_r.right = s.left
                    velX = 0
        screen.blit(text, (200, 100))
        screen.blit(text1, (250,200))
        screen.blit(text2, (100,300))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
    pygame.quit()