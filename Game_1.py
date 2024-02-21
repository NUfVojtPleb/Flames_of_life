import pygame, sys, random, time


# Matches
class Match(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.animation = False
        self.sprites = []
        for i in range(9):
            i = i + 1
            self.picture = pygame.image.load(f"Sirka/Sirka{i}.png")
            self.finale_picture = pygame.transform.scale(
                self.picture,
                (self.picture.get_width() // 2, self.picture.get_height() // 2),
            )
            self.sprites.append(self.finale_picture)
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def animation_statement(self):
        self.animation = True

    def update(self, speed):
        if self.animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 8
                self.animation = False

        self.image = self.sprites[int(self.current_sprite)]


# Matches for level 3
class Match_level_3(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.animation = False
        self.sprites = []
        for i in range(9):
            i = i + 1
            self.picture = pygame.image.load(f"Sirka/Sirka{i}.png")
            self.finale_picture = pygame.transform.scale(
                self.picture,
                (self.picture.get_width() // 2.5, self.picture.get_height() // 2.5),
            )
            self.sprites.append(self.finale_picture)
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def animation_statement(self):
        self.animation = True

    def update(self, speed):
        if self.animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 8
                self.animation = False

        self.image = self.sprites[int(self.current_sprite)]


# Opponent / death + explosion
class Exponent(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.animation = False
        self.sprites = []
        self.first_picture = pygame.image.load(f"opponent/opponent2.png")
        self.win = pygame.image.load(f"winer winer chicken dinner/You winblb.png")
        self.finallwin = pygame.transform.scale(
            self.win, (self.win.get_width() // 1.1, self.win.get_height() // 1.1)
        )
        self.sprites.append(self.first_picture)
        for i in range(5):
            i = i + 1
            self.picture = pygame.image.load(f"Expo/exp{i}.png")

            self.finale_picture = pygame.transform.scale(
                self.picture,
                (self.picture.get_width() * 3, self.picture.get_height() * 3),
            )
            self.sprites.append(self.finale_picture)
        self.sprites.append(self.finallwin)
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def animation_statement(self):
        self.animation = True

    def update(self, speed, pos_x, pos_y):
        if self.animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 6
                if self.current_sprite == 6:
                    self.rect = self.image.get_rect()
                    self.rect.topleft = [pos_x, pos_y]
                self.animation = False

        self.image = self.sprites[int(self.current_sprite)]


# buttons
class Buttons(pygame.sprite.Sprite):
    def __init__(self, number, pos_x, pos_y):
        super().__init__()
        if number == 1:
            self.image = pygame.image.load("Button/Button_1.png")
        if number == 2:
            self.image = pygame.image.load("Button/Button_2.png")
        if number == 3:
            self.image = pygame.image.load("Button/Button_3.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]


# Intro_buttons
class Intro_Buttons(pygame.sprite.Sprite):
    def __init__(self, number, pos_x, pos_y):
        super().__init__()
        if number == 1:
            self.image = pygame.image.load("Buttons_for_intro/Text_Button_1.png")
        if number == 2:
            self.image = pygame.image.load("Buttons_for_intro/Text_Button_2.png")
        if number == 3:
            self.image = pygame.image.load("Buttons_for_intro/Text_Button_3.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]


# Intro_buttons
class Menu_Buttons(pygame.sprite.Sprite):
    def __init__(self, number, pos_x, pos_y):
        super().__init__()
        if number == 1:
            self.image = pygame.image.load("Buttons_for_menu/Level_1_button.png")
        if number == 2:
            self.image = pygame.image.load("Buttons_for_menu/Level_2_button.png")
        if number == 3:
            self.image = pygame.image.load("Buttons_for_menu/Level_3_button.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]


# pointer
class Pointer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Pointer/cursor.png")
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


# flames
class Flamse(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("Flame/flame2.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]


# Lose animation
class Lose(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("winer winer chicken dinner/you looseblb.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]


# Arrow_left
class Arrow_left(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("Arrows/arrow_left.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]


# Arrow_right
class Arrow_right(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("Arrows/arrow_right.png")
        self.finallimage = pygame.transform.scale(
            self.image, (self.image.get_width() * 2, self.image.get_height() * 2)
        )
        self.image_2 = self.finallimage
        self.rect = self.image_2.get_rect()
        self.rect.topleft = [pos_x, pos_y]


# Title
class Title(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("Text/title.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]


# Rules
class Rules(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("Text/rules.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]


# Game_Statment
class Game_Statment:
    def __init__(self):
        self.state = "intro"
        self.button_statment = True
        self.is_paused = False
        self.pause_start_time = 0

    # intro screen
    def intro(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if intro_button_1.rect.collidepoint(event.pos):
                    self.state = "game_levels"
                elif intro_button_2.rect.collidepoint(event.pos):
                    self.state = "rules_slide"
                elif intro_button_3.rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        screen.blit(background_1, (0, 0))
        intro_buttons_group.draw(screen)
        title_group.draw(screen)
        cursor_group.draw(screen)
        cursor_group.update()
        pygame.display.flip()

    # rules_screen
    def rules_slide(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if arrow_left.rect.collidepoint(event.pos):
                    self.state = "intro"
        screen.blit(background_1, (0, 0))
        arrow_group_left.draw(screen)
        rules_group.draw(screen)
        cursor_group.draw(screen)
        cursor_group.update()
        pygame.display.flip()

    # game_levels_screen
    def game_levels(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_button1.rect.collidepoint(event.pos):
                    self.state = "level_1"
                elif menu_button2.rect.collidepoint(event.pos):
                    self.state = "level_2"
                elif menu_button3.rect.collidepoint(event.pos):
                    self.state = "level_3"
                elif arrow_left.rect.collidepoint(event.pos):
                    self.state = "intro"

        screen.blit(background_1, (0, 0))
        menu_buttons_group.draw(screen)
        arrow_group_left.draw(screen)
        cursor_group.draw(screen)
        cursor_group.update()
        pygame.display.flip()

    # level_1
    def level_1(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if len(list_of_matches_1) == 0:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if arrow_right.rect.collidepoint(event.pos):
                        self.state = "intro"
                        winner_statement_level_1.insert(0, 2)
                        moving_sprites_1.empty()
                        listofexpo.pop(0)
                        for i in range(12):
                            i = i + 1
                            match_1 = Match(x_1 * i, y_1)
                            moving_sprites_1.add(match_1)
                            list_of_matches_1.append(match_1)
                        add_buttons3()
                        expo_group.empty()
                        for i in range(1):
                            expo = Exponent(650, 0)
                            expo_group.add(expo)
                            listofexpo.append(expo)

            elif len(list_of_matches_1) == 1:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_statment == False:
                        pass
                    else:
                        if button1.rect.collidepoint(event.pos):
                            z = 1
                            for i in range(z):
                                sirka = list_of_matches_1[i]
                                sirka.animation_statement()
                            for i in range(z):
                                list_of_matches_1.pop(0)
                            hide_buttons2()
                            self.is_paused = not self.is_paused
                            if self.is_paused:
                                self.pause_start_time = time.time()

            elif len(list_of_matches_1) == 2:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_statment == False:
                        pass
                    else:
                        if button1.rect.collidepoint(event.pos):
                            z = 1
                            for i in range(z):
                                sirka = list_of_matches_1[i]
                                sirka.animation_statement()
                            for i in range(z):
                                list_of_matches_1.pop(0)
                            hide_buttons3()
                            self.is_paused = not self.is_paused
                            if self.is_paused:
                                self.pause_start_time = time.time()

                        if button2.rect.collidepoint(event.pos):
                            z = 2
                            for i in range(z):
                                sirka = list_of_matches_1[i]
                                sirka.animation_statement()
                            for i in range(z):
                                list_of_matches_1.pop(0)
                            hide_buttons3()
                            self.is_paused = not self.is_paused
                            if self.is_paused:
                                self.pause_start_time = time.time()

            elif len(list_of_matches_1) >= 3:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_statment == False:
                        pass
                    else:
                        if button1.rect.collidepoint(event.pos):
                            z = 1
                            for i in range(z):
                                sirka = list_of_matches_1[i]
                                sirka.animation_statement()
                            for i in range(z):
                                list_of_matches_1.pop(0)

                            self.is_paused = not self.is_paused
                            if self.is_paused:
                                self.pause_start_time = time.time()

                        if button2.rect.collidepoint(event.pos):
                            z = 2
                            for i in range(z):
                                sirka = list_of_matches_1[i]
                                sirka.animation_statement()
                            for i in range(z):
                                list_of_matches_1.pop(0)

                            self.is_paused = not self.is_paused
                            if self.is_paused:
                                self.pause_start_time = time.time()

                        if button3.rect.collidepoint(event.pos):
                            z = 3
                            for i in range(z):
                                sirka = list_of_matches_1[i]
                                sirka.animation_statement()
                            for i in range(z):
                                list_of_matches_1.pop(0)
                            self.is_paused = not self.is_paused
                            if self.is_paused:
                                self.pause_start_time = time.time()
        # pause manager
        if self.is_paused:
            hide_buttons1()

            # Check if 3 seconds have passed
            if time.time() - self.pause_start_time > 3:
                self.is_paused = False
                opponent_level_1()
                if len(list_of_matches_1) == 0:
                    hide_buttons1()
                elif len(list_of_matches_1) == 1:
                    add_buttons1()
                elif len(list_of_matches_1) == 2:
                    add_buttons2()
                else:
                    add_buttons3()

        screen.blit(background_1, (0, 0))
        expo_group.draw(screen)
        if winner_statement_level_1[0] == 0:
            expoloze = listofexpo[0]
            expoloze.animation_statement()
            expo_group.update(0.3, 350, 0)
            arrow_group_right.draw(screen)
        elif winner_statement_level_1[0] == 1:
            lose_group.draw(screen)
            arrow_group_right.draw(screen)
        moving_sprites_1.draw(screen)
        moving_sprites_1.update(0.35)
        buttons_group.draw(screen)
        flame_group.draw(screen)
        cursor_group.draw(screen)
        cursor_group.update()

        pygame.display.flip()

    # level_2
    def level_2(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if len(list_of_matches_2) == 0:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if arrow_right.rect.collidepoint(event.pos):
                        self.state = "intro"
                        winner_statement_level_2.insert(0, 2)
                        moving_sprites_2.empty()
                        listofexpo.pop(0)
                        for i in range(16):
                            i = i + 1
                            match_2 = Match(x_2 * i, y_2)
                            moving_sprites_2.add(match_2)
                            list_of_matches_2.append(match_2)
                        add_buttons3()
                        expo_group.empty()
                        for i in range(1):
                            expo = Exponent(650, 0)
                            expo_group.add(expo)
                            listofexpo.append(expo)

            elif len(list_of_matches_2) == 1:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_statment == False:
                        pass
                    else:
                        if button1.rect.collidepoint(event.pos):
                            z = 1
                            for i in range(z):
                                sirka = list_of_matches_2[i]
                                sirka.animation_statement()
                            for i in range(z):
                                list_of_matches_2.pop(0)
                            hide_buttons2()
                            self.is_paused = not self.is_paused
                            if self.is_paused:
                                self.pause_start_time = time.time()

            elif len(list_of_matches_2) == 2:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_statment == False:
                        pass
                    else:
                        if button1.rect.collidepoint(event.pos):
                            z = 1
                            for i in range(z):
                                sirka = list_of_matches_2[i]
                                sirka.animation_statement()
                            for i in range(z):
                                list_of_matches_2.pop(0)
                            hide_buttons3()
                            self.is_paused = not self.is_paused
                            if self.is_paused:
                                self.pause_start_time = time.time()

                        if button2.rect.collidepoint(event.pos):
                            z = 2
                            for i in range(z):
                                sirka = list_of_matches_2[i]
                                sirka.animation_statement()
                            for i in range(z):
                                list_of_matches_2.pop(0)
                            hide_buttons3()
                            self.is_paused = not self.is_paused
                            if self.is_paused:
                                self.pause_start_time = time.time()

            elif len(list_of_matches_2) >= 3:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_statment == False:
                        pass
                    else:
                        if button1.rect.collidepoint(event.pos):
                            z = 1
                            for i in range(z):
                                sirka = list_of_matches_2[i]
                                sirka.animation_statement()
                            for i in range(z):
                                list_of_matches_2.pop(0)

                            self.is_paused = not self.is_paused
                            if self.is_paused:
                                self.pause_start_time = time.time()

                        if button2.rect.collidepoint(event.pos):
                            z = 2
                            for i in range(z):
                                sirka = list_of_matches_2[i]
                                sirka.animation_statement()
                            for i in range(z):
                                list_of_matches_2.pop(0)

                            self.is_paused = not self.is_paused
                            if self.is_paused:
                                self.pause_start_time = time.time()

                        if button3.rect.collidepoint(event.pos):
                            z = 3
                            for i in range(z):
                                sirka = list_of_matches_2[i]
                                sirka.animation_statement()
                            for i in range(z):
                                list_of_matches_2.pop(0)
                            self.is_paused = not self.is_paused
                            if self.is_paused:
                                self.pause_start_time = time.time()

        # pause manager
        if self.is_paused:
            hide_buttons1()

            # Check if 3 seconds have passed
            if time.time() - self.pause_start_time > 3:
                self.is_paused = False
                opponent_level_2()
                if len(list_of_matches_2) == 0:
                    hide_buttons1()
                elif len(list_of_matches_2) == 1:
                    add_buttons1()
                elif len(list_of_matches_2) == 2:
                    add_buttons2()
                else:
                    add_buttons3()

        screen.blit(background_1, (0, 0))
        expo_group.draw(screen)
        if winner_statement_level_2[0] == 0:
            expoloze = listofexpo[0]
            expoloze.animation_statement()
            expo_group.update(0.3, 350, 0)
            arrow_group_right.draw(screen)
        elif winner_statement_level_2[0] == 1:
            lose_group.draw(screen)
            arrow_group_right.draw(screen)
        moving_sprites_2.draw(screen)
        moving_sprites_2.update(0.35)
        buttons_group.draw(screen)
        flame_group.draw(screen)

        cursor_group.draw(screen)
        cursor_group.update()

        pygame.display.flip()

    # level_3
    def level_3(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if len(list_of_matches_3) == 0:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if arrow_right.rect.collidepoint(event.pos):
                        self.state = "intro"
                        winner_statement_level_3.insert(0, 2)
                        moving_sprites_3.empty()
                        listofexpo.pop(0)
                        for i in range(24):
                            i = i + 1
                            match_3 = Match_level_3(x_3 * i, y_3)
                            moving_sprites_3.add(match_3)
                            list_of_matches_3.append(match_3)
                        add_buttons3()
                        expo_group.empty()
                        for i in range(1):
                            expo = Exponent(650, 0)
                            expo_group.add(expo)
                            listofexpo.append(expo)

            elif len(list_of_matches_3) == 1:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_statment == False:
                        pass
                    else:
                        if button1.rect.collidepoint(event.pos):
                            z = 1
                            for i in range(z):
                                sirka = list_of_matches_3[i]
                                sirka.animation_statement()
                            for i in range(z):
                                list_of_matches_3.pop(0)
                            hide_buttons2()
                            self.is_paused = not self.is_paused
                            if self.is_paused:
                                self.pause_start_time = time.time()

            elif len(list_of_matches_3) == 2:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_statment == False:
                        pass
                    else:
                        if button1.rect.collidepoint(event.pos):
                            z = 1
                            for i in range(z):
                                sirka = list_of_matches_3[i]
                                sirka.animation_statement()
                            for i in range(z):
                                list_of_matches_3.pop(0)
                            hide_buttons3()
                            self.is_paused = not self.is_paused
                            if self.is_paused:
                                self.pause_start_time = time.time()

                        if button2.rect.collidepoint(event.pos):
                            z = 2
                            for i in range(z):
                                sirka = list_of_matches_3[i]
                                sirka.animation_statement()
                            for i in range(z):
                                list_of_matches_3.pop(0)
                            hide_buttons3()
                            self.is_paused = not self.is_paused
                            if self.is_paused:
                                self.pause_start_time = time.time()

            elif len(list_of_matches_3) >= 3:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_statment == False:
                        pass
                    else:
                        if button1.rect.collidepoint(event.pos):
                            z = 1
                            for i in range(z):
                                sirka = list_of_matches_3[i]
                                sirka.animation_statement()
                            for i in range(z):
                                list_of_matches_3.pop(0)

                            self.is_paused = not self.is_paused
                            if self.is_paused:
                                self.pause_start_time = time.time()

                        if button2.rect.collidepoint(event.pos):
                            z = 2
                            for i in range(z):
                                sirka = list_of_matches_3[i]
                                sirka.animation_statement()
                            for i in range(z):
                                list_of_matches_3.pop(0)

                            self.is_paused = not self.is_paused
                            if self.is_paused:
                                self.pause_start_time = time.time()

                        if button3.rect.collidepoint(event.pos):
                            z = 3
                            for i in range(z):
                                sirka = list_of_matches_3[i]
                                sirka.animation_statement()
                            for i in range(z):
                                list_of_matches_3.pop(0)
                            self.is_paused = not self.is_paused
                            if self.is_paused:
                                self.pause_start_time = time.time()
        # pause manager
        if self.is_paused:
            hide_buttons1()

            # Check if 3 seconds have passed
            if time.time() - self.pause_start_time > 3:
                self.is_paused = False
                opponent_level_3()
                if len(list_of_matches_3) == 0:
                    hide_buttons1()
                elif len(list_of_matches_3) == 1:
                    add_buttons1()
                elif len(list_of_matches_3) == 2:
                    add_buttons2()
                else:
                    add_buttons3()

        screen.blit(background_1, (0, 0))
        expo_group.draw(screen)
        if winner_statement_level_3[0] == 0:
            expoloze = listofexpo[0]
            expoloze.animation_statement()
            expo_group.update(0.3, 350, 0)
            arrow_group_right.draw(screen)
        elif winner_statement_level_3[0] == 1:
            lose_group.draw(screen)
            arrow_group_right.draw(screen)
        moving_sprites_3.draw(screen)
        moving_sprites_3.update(0.35)
        buttons_group.draw(screen)
        flame_group.draw(screen)

        cursor_group.draw(screen)
        cursor_group.update()

        pygame.display.flip()

    # state_manager
    def state_manager(self):
        if self.state == "intro":
            self.intro()
        elif self.state == "game_levels":
            self.game_levels()
        elif self.state == "rules_slide":
            self.rules_slide()
        elif self.state == "level_1":
            self.level_1()
        elif self.state == "level_2":
            self.level_2()
        elif self.state == "level_3":
            self.level_3()


# button annulment


def hide_buttons1():
    game_state.button_statment = False
    buttons_group.remove(button1)
    buttons_group.remove(button2)
    buttons_group.remove(button3)
    flame_group.remove(flame)
    flame_group.remove(flame1)
    flame_group.remove(flame2)
    flame_group.remove(flame3)
    flame_group.remove(flame4)
    flame_group.remove(flame5)


def hide_buttons2():
    game_state.button_statment = False
    buttons_group.remove(button2)
    flame_group.remove(flame1)
    flame_group.remove(flame2)
    buttons_group.remove(button3)
    flame_group.remove(flame3)
    flame_group.remove(flame4)
    flame_group.remove(flame5)


def hide_buttons3():
    game_state.button_statment = False
    buttons_group.remove(button3)
    flame_group.remove(flame3)
    flame_group.remove(flame4)
    flame_group.remove(flame5)


def add_buttons1():
    game_state.button_statment = True
    buttons_group.add(button1)
    flame_group.add(flame)


def add_buttons2():
    game_state.button_statment = True
    buttons_group.add(button1)
    buttons_group.add(button2)
    flame_group.add(flame)
    flame_group.add(flame1)
    flame_group.add(flame2)


def add_buttons3():
    game_state.button_statment = True
    buttons_group.add(button1)
    buttons_group.add(button2)
    buttons_group.add(button3)
    flame_group.add(flame)
    flame_group.add(flame1)
    flame_group.add(flame2)
    flame_group.add(flame3)
    flame_group.add(flame4)
    flame_group.add(flame5)


# winner_statement_level_1

winner_statement_level_1 = [2]

# winner_statement_level_2

winner_statement_level_2 = [2]

# winner_statement_level_3

winner_statement_level_3 = [3]


# Computer/ Opponent/ control functin


# opponent_level_1
def opponent_level_1():
    x = random.randint(1, 3)
    if len(list_of_matches_1) == 3:
        for i in range(2):
            sirka = list_of_matches_1[i]
            sirka.animation_statement()
        for i in range(2):
            list_of_matches_1.pop(0)
        hide_buttons2()

    elif len(list_of_matches_1) == 2:
        sirka = list_of_matches_1[0]
        sirka.animation_statement()
        list_of_matches_1.pop(0)
        hide_buttons2()

    elif len(list_of_matches_1) == 1:
        sirka = list_of_matches_1[0]
        sirka.animation_statement()
        list_of_matches_1.pop(0)
        hide_buttons1()
        winner_statement_level_1.insert(0, 0)
        # pygame.quit()
        # sys.exit()

    elif len(list_of_matches_1) == 0:
        hide_buttons1()
        winner_statement_level_1.insert(0, 1)
        # pygame.quit()
        # sys.exit()

    else:
        for i in range(x):
            sirka = list_of_matches_1[i]
            sirka.animation_statement()
        for i in range(x):
            list_of_matches_1.pop(0)
        if len(list_of_matches_1) == 2:
            hide_buttons3()
        elif len(list_of_matches_1) == 1:
            hide_buttons2()


# opponent_level_2
def opponent_level_2():
    x = random.randint(1, 3)
    if len(list_of_matches_2) == 3:
        for i in range(2):
            sirka = list_of_matches_2[i]
            sirka.animation_statement()
        for i in range(2):
            list_of_matches_2.pop(0)
        hide_buttons2()

    elif len(list_of_matches_2) == 2:
        sirka = list_of_matches_2[0]
        sirka.animation_statement()
        list_of_matches_2.pop(0)
        hide_buttons2()

    elif len(list_of_matches_2) == 1:
        sirka = list_of_matches_2[0]
        sirka.animation_statement()
        list_of_matches_2.pop(0)
        hide_buttons1()
        winner_statement_level_2.insert(0, 0)
        # pygame.quit()
        # sys.exit()

    elif len(list_of_matches_2) == 0:
        hide_buttons1()
        winner_statement_level_2.insert(0, 1)
        # pygame.quit()
        # sys.exit()

    else:
        for i in range(x):
            sirka = list_of_matches_2[i]
            sirka.animation_statement()
        for i in range(x):
            list_of_matches_2.pop(0)
        if len(list_of_matches_2) == 2:
            hide_buttons3()
        elif len(list_of_matches_2) == 1:
            hide_buttons2()


# opponent_level_3
def opponent_level_3():
    x = random.randint(1, 3)
    if len(list_of_matches_3) == 3:
        for i in range(2):
            sirka = list_of_matches_3[i]
            sirka.animation_statement()
        for i in range(2):
            list_of_matches_3.pop(0)
        hide_buttons2()

    elif len(list_of_matches_3) == 2:
        sirka = list_of_matches_3[0]
        sirka.animation_statement()
        list_of_matches_3.pop(0)
        hide_buttons2()

    elif len(list_of_matches_3) == 1:
        sirka = list_of_matches_3[0]
        sirka.animation_statement()
        list_of_matches_3.pop(0)
        hide_buttons1()
        winner_statement_level_3.insert(0, 0)
        # pygame.quit()
        # sys.exit()

    elif len(list_of_matches_3) == 0:
        hide_buttons1()
        winner_statement_level_3.insert(0, 1)
        # pygame.quit()
        # sys.exit()

    else:
        for i in range(x):
            sirka = list_of_matches_3[i]
            sirka.animation_statement()
        for i in range(x):
            list_of_matches_3.pop(0)
        if len(list_of_matches_3) == 2:
            hide_buttons3()
        elif len(list_of_matches_3) == 1:
            hide_buttons2()


# General Setup
pygame.init()
clock = pygame.time.Clock()
game_state = Game_Statment()
# Colores
PURPLE = (54, 19, 84)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 102, 0)
RED = (196, 30, 58)
BLUE = (0, 0, 255)
ORANGE = (212, 175, 55)

# Game Screen
WIDTH, HEIGHT = 1600, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background_1 = pygame.image.load("Background/pxfuel6.jpg")
background_2 = pygame.image.load("Background/Intro.png")
pygame.display.set_caption("Match Animation")
pygame.mouse.set_visible(False)

# Creating the sprites and groups

# Matches_for_level_1
moving_sprites_1 = pygame.sprite.Group()

x_1, y_1 = 113, 275

list_of_matches_1 = []

for i in range(12):
    i = i + 1
    match_1 = Match(x_1 * i, y_1)
    moving_sprites_1.add(match_1)
    list_of_matches_1.append(match_1)

# Matches_for level_2
moving_sprites_2 = pygame.sprite.Group()

x_2, y_2 = 85, 275

list_of_matches_2 = []

for i in range(16):
    i = i + 1
    match_2 = Match(x_2 * i, y_2)
    moving_sprites_2.add(match_2)
    list_of_matches_2.append(match_2)

# Matches_for level_2
moving_sprites_3 = pygame.sprite.Group()

x_3, y_3 = 60, 275

list_of_matches_3 = []

for i in range(24):
    i = i + 1
    match_3 = Match_level_3(x_3 * i, y_3)
    moving_sprites_3.add(match_3)
    list_of_matches_3.append(match_3)


# Exponent
expo_group = pygame.sprite.Group()

listofexpo = []
for i in range(1):
    expo = Exponent(650, 0)
    expo_group.add(expo)
    listofexpo.append(expo)

# Buttons
buttons_group = pygame.sprite.Group()
button1 = Buttons(1, 100, 700)
buttons_group.add(button1)

button2 = Buttons(2, 600, 700)
buttons_group.add(button2)

button3 = Buttons(3, 1100, 700)
buttons_group.add(button3)

# Intro Buttons
intro_buttons_group = pygame.sprite.Group()
intro_button_1 = Intro_Buttons(1, 550, 300)
intro_buttons_group.add(intro_button_1)

intro_button_2 = Intro_Buttons(2, 550, 500)
intro_buttons_group.add(intro_button_2)

intro_button_3 = Intro_Buttons(3, 550, 700)
intro_buttons_group.add(intro_button_3)

# Menu Buttons
menu_buttons_group = pygame.sprite.Group()
menu_button1 = Menu_Buttons(1, 350, 38)
menu_buttons_group.add(menu_button1)
menu_button2 = Menu_Buttons(2, 350, 326)
menu_buttons_group.add(menu_button2)
menu_button3 = Menu_Buttons(3, 350, 614)
menu_buttons_group.add(menu_button3)
# Pointer

cursor_group = pygame.sprite.Group()
cursor = Pointer()
cursor_group.add(cursor)

# Flames

flame_group = pygame.sprite.Group()

flame = Flamse(265, 730)
flame1 = Flamse(700, 730)
flame2 = Flamse(825, 730)
flame3 = Flamse(1150, 730)
flame4 = Flamse(1265, 730)
flame5 = Flamse(1380, 730)
flame_group.add(flame)
flame_group.add(flame1)
flame_group.add(flame2)
flame_group.add(flame3)
flame_group.add(flame4)
flame_group.add(flame5)

# Lose
lose_group = pygame.sprite.Group()
lose = Lose(300, 600)
lose_group.add(lose)

# arrow

arrow_group_right = pygame.sprite.Group()
arrow_right = Arrow_right(1400, 730)
arrow_group_right.add(arrow_right)

arrow_group_left = pygame.sprite.Group()
arrow_left = Arrow_left(85, 730)
arrow_group_left.add(arrow_left)

# Text
title_group = pygame.sprite.Group()
title = Title(314, 15)
title_group.add(title)

# Rules_text

rules_group = pygame.sprite.Group()
rules = Rules(0, 315)
rules_group.add(rules)

# conditions for game loop

running = True

# Game Loop
while running:
    game_state.state_manager()
    clock.tick(60)
