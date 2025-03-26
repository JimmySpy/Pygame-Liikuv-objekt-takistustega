#Jimmy Ode
#Git hub = https://github.com/JimmySpy

import pygame, sys, random  # Impordib vajalikud moodulid
from button import Button  # Impordib Button klassi nupu kasutamiseks

pygame.init()  # Initsialiseerib Pygame'i

# Ekraani seaded
SCREENWIDTH, SCREENHEIGHT = 1280, 720  # Määrab ekraani laiuse ja kõrguse
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))  # Loob mänguakna
pygame.display.set_caption("Menu")  # Seab mänguakna nimeks "Menu"

# Laadib taustapildi
BG = pygame.image.load("assets/Background.png")


# Funktsioon kindla suurusega fondi saamiseks
def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)


# Peamine mängufunktsioon
def play():
    # Mängija seaded
    player_size = 30
    player_x = SCREENWIDTH // 2  # Mängija algpositsioon ekraani keskel
    player_y = SCREENHEIGHT // 2
    player_speed = 5  # Mängija liikumiskiirus
    player_color = (0, 0, 255)  # Mängija värv (sinine)

    # Takistuste seaded
    num_obstacles = 10  # Takistuste arv
    obstacle_size = 50
    obstacles = []
    obstacle_speeds = []

    # Skoori seaded
    score = 0
    highest_score = 0
    try:
        with open("highscore.txt", "r") as file:
            highest_score = int(file.read())  # Laeb kõrgeima skoori failist
    except FileNotFoundError:
        highest_score = 0  # Kui faili pole, alustatakse nullist

    # Genereerib takistused juhuslike positsioonide ja liikumissuundadega
    for _ in range(num_obstacles):
        x = random.randint(0, SCREENWIDTH - obstacle_size)
        y = random.randint(0, SCREENHEIGHT - obstacle_size)
        dx = random.choice([-3, 3])  # Juhuslik liikumiskiirus X teljel
        dy = random.choice([-3, 3])  # Juhuslik liikumiskiirus Y teljel
        obstacles.append(pygame.Rect(x, y, obstacle_size, obstacle_size))
        obstacle_speeds.append((dx, dy))

    running = True  # Määrab mängu töötavaks
    while running:
        pygame.time.delay(30)  # Lisab väikese pausi mängutsüklisse
        SCREEN.fill((255, 255, 255))  # Taust on valge
        score += 1  # Suurendab skoori ajaga

        # Kontrollib sündmusi (nt akna sulgemine)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Mängija liikumine nooleklahvide abil
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_UP]:
            player_y -= player_speed
        if keys[pygame.K_DOWN]:
            player_y += player_speed

        # Kontrollib, kas mängija põrkab takistusega
        player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
        for obs in obstacles:
            if player_rect.colliderect(obs):
                player_color = (255, 0, 0)  # Muudab mängija punaseks
                running = False  # Lõpetab mängu

        # Liigutab takistusi ja muudab suunda, kui need jõuavad ekraani servani
        for i, obs in enumerate(obstacles):
            dx, dy = obstacle_speeds[i]
            obs.x += dx
            obs.y += dy
            if obs.left <= 0 or obs.right >= SCREENWIDTH:
                obstacle_speeds[i] = (-dx, dy)
            if obs.top <= 0 or obs.bottom >= SCREENHEIGHT:
                obstacle_speeds[i] = (dx, -dy)

        # Joonistab takistused ja mängija ekraanile
        for obs in obstacles:
            pygame.draw.rect(SCREEN, (0, 0, 0), obs)
        pygame.draw.rect(SCREEN, player_color, player_rect)

        # Kuvab skoori
        score_text = get_font(30).render(f"Score: {score}", True, (0, 0, 0))
        SCREEN.blit(score_text, (10, 10))
        highest_score_text = get_font(30).render(f"Highest Score: {highest_score}", True, (0, 0, 0))
        SCREEN.blit(highest_score_text, (10, 50))

        pygame.display.update()

    # Salvestab uue kõrgeima skoori, kui see ületati
    if score > highest_score:
        highest_score = score
        with open("highscore.txt", "w") as file:
            file.write(str(highest_score))

    main_menu()  # Tagasi peamenüüsse


# Funktsioon valikute (options) menüü jaoks
def options():
    while True:
        SCREEN.fill("white")
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        OPTIONS_BACK = Button(image=None, pos=(640, 460), text_input="BACK", font=get_font(75), base_color="Black",
                              hovering_color="Green")
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                main_menu()

        pygame.display.update()


# Peamenüü funktsioon
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        # Loob nupud
        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), text_input="PLAY",
                             font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), text_input="QUIT",
                             font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()  # Käivitab peamenüü
