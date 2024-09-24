import pygame, random

pygame.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Feed The Dragon")

coin_veloity = 10



FPS = 60
clock = pygame.time.Clock()
PLAYER_STARTING_LIVES = 5

PLAYER_VELOCITY = 10
COIN_STARTING_VELOCITY = 10
COIN_ACCELERATION = 0.5
SCORE = 0
PLAYER_LIVES = 5
COIN_VELOCITY = 5
BUFFER_DISTANCE = 100
lives_text = 5
GREEN = (0, 255, 0)
DARK_GREEN = (10, 50, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


font = pygame.font.Font('AttackGraffiti.ttf', 32)

TRACKS_SCORE = font.render("Score: " + str(SCORE), True, GREEN, DARK_GREEN)
score_rect = SCORE.get_rect()
SCORE.topleft = (10, 10)
Background = DARK_GREEN

color = GREEN
BACK_GROUND = DARK_GREEN
game_over_text = "GAMEOVER"
game_over_rect = game_over_text




Center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
title_rect.centerx = WINDOW_WIDTH//2
title_rect.y = 10

coin_sound = pygame.mixer.Sound("coin_sound.wav")
miss_sound = pygame.mixer.Sound("miss_sound.wav")
pygame.mixer.music.load("ftd_background_music.wav")

player_image = pygame.image.load("dragon_right.png")
player_rect = player_image.get_rect()
player_rect.left = 32
player_rect.centery = WINDOW_HEIGHT // 2
coin_image = "coin_image"
coin_rect = "coin_rect"
coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)






pygame.mixer.music.play(-1, 0.0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.k_UP] and player_rect.top > 64:
        player_rect.y -=PLAYER_VELOCITY
    if keys[pygame.k_DOWN] and player_rect.bottom < WINDOW_HEIGHT:


    if coin_rect.x < 0:
        PLAYER_LIVES -= 1
        miss_sound.play()
        coin_rect.x = WINDOW_WIDTH + WINDOW_HEIGHT
        coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)

    score_text = font.render("Score: " + str(SCORE), True, GREEN, DARK_GREEN)
    lives_text = font.render("Lives: " + str(PLAYER_LIVES), True, GREEN, DARK_GREEN)
    if PLAYER_LIVES == 0:
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, contnue_rect)
        pygame.display.update()


        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    score = 0
                    player_lives = PLAYER_STARTING_LIVES
                    player_rect.y = WINDOW_HEIGHT // 2
                    coin_velocity = COIN_STARTING_VELOCITY
                    pygame.mixer.music.play(-1, 0.0)
                    is_paused = False
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False




    else:
        coin_rect.x -= coin_veloity

    if player_rect.colliderect(coin_rect):
        SCORE += 1
        coin_sound.play()



        player_rect.x += PLAYER_VELOCITY
        display_surface.fill(BLACK)


    pygame.draw.line(display_surface, WHITE, (0, 64), (WINDOW_WIDTH, 64), 2)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(lives_text, lives_rect)
    display_surface.blit(SCORE, score_rect)
    display_surface.blit(TRACKS_SCORE, SCORE)
    display_surface.blit(lives_text, lives_rect)



pygame.display.update()
clock.tick(FPS)


pygame.quit()