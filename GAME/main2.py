def level_the_global1():
    from GAME.room import level_the_room
    import pygame
    pygame.init()
    wall_width = 32
    wall_height = 32
    step = 10
    step1 = 10
    screen = pygame.display.set_mode([1248, 960])
    fon = pygame.image.load("GAME/texturse/fon.png")
    fon = pygame.transform.scale(fon, (1248, 960))

    stone = pygame.image.load("GAME/texturse/мрамор итальянский.jpg")
    stone = pygame.transform.scale(stone, (wall_width, wall_height))

    ezhidze = pygame.image.load("GAME/texturse/ezhidze.png")
    ezhidze = pygame.transform.scale(ezhidze, (64, 64))
    ezhidze_r = ezhidze.get_rect(topleft=(1000, 64))

    lesenka = pygame.image.load("GAME/texturse/лестница.png")
    lesenka = pygame.transform.scale(lesenka, (wall_width, wall_height))

    door_close_down = pygame.image.load("GAME/texturse/doors/door_close2.png")
    door_close_down = pygame.transform.scale(door_close_down, (wall_width, wall_height))
    door_close_up = pygame.image.load("GAME/texturse/doors/door_close1.png")
    door_close_up = pygame.transform.scale(door_close_up, (wall_width, wall_height))
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
             "*        |                            *",
             "*        /                            *",
             "*---***********************************",
             "*---                                  *",
             "*---                                  *",
             "***********************************---*",
             "*                                  ---*",
             "*                                  ---*",
             "*---***********************************",
             "*---                                  *",
             "*---                                  *",
             "***********************************---*",
             "*                                  ---*",
             "*                                  ---*",
             "*---***********************************",
             "*---                                  *",
             "*---                                  *",
             "***********************************---*",
             "*                                  ---*",
             "*                                  ---*",
             "*---***********************************",
             "*---                                  *",
             "*---                                  *",
             "***********************************---*",
             "*                                  ---*",
             "*                                  ---*",
             "***************************************",
             "***************************************"]
    stop = []
    lesenka_list = []
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
                if col == "/":
                    screen.blit(door_close_down, (x, y))
                if col == "|":
                    door_r = door_close_down.get_rect(topleft=(x, y))
                    screen.blit(door_close_up, door_r)
                if col == "-":
                    lesenka_r = lesenka.get_rect(topleft=(x, y))
                    lesenka_list.append(lesenka_r)
                    screen.blit(lesenka, lesenka_r)
                x += wall_width
            y += wall_height
            x = 0
        screen.blit(ezhidze, ezhidze_r)

        ezhidze_r.x = ezhidze_r.x + step1
        if ezhidze_r.x < 32 or ezhidze_r.x > 1184:
            step1 = -step1

        if player_r.colliderect(ezhidze_r):
            screen.fill([255, 0, 0])
            player_r.x = 32
            player_r.y = 830
            pygame.time.get_ticks()
            pygame.time.delay(250)

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

        if player_r.collidelist(lesenka_list) and keys[pygame.K_w]:
            velY = -step
        if player_r.collidelist(lesenka_list) and keys[pygame.K_s]:
            velY = step
        player_r.y = player_r.y + velY

        if player_r.colliderect(door_r) and keys[pygame.K_e]:
            level_the_room()
        for s in stop:
            if player_r.colliderect(s):
                if velY < 0:
                    player_r.top = s.bottom
                    velY = 0
                elif velY > 0:
                    player_r.bottom = s.top
                    velY = 0

        for s in stop:
            if player_r.colliderect(s):
                if velX < 0:
                    player_r.left = s.right
                    velX = 0
                elif velX > 0:
                    player_r.right = s.left
                    velX = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
    pygame.quit()