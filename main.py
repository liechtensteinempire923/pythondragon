import pygame

pygame.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Feed The Dragon")


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
game_over_text = "GAMEOVER"
Background = DARK_GREEN

color = GREEN
BACK_GROUND = DARK_GREEN

Center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)


coin_sound = pygame.mixer.Sound("coin_sound.wav")
miss_sound = pygame.mixer.Sound("miss_sound.wav")
pygame.mixer.music.load("ftd_background_music.wav")

player_image = pygame.image.load("dragon_right.png")
player_rect = player_image.get_rect()
player_rect.left = 32
player_rect.centery = WINDOW_HEIGHT // 2
coin_image = "coin_image"
coin_rect = "coin_rect"







pygame.mixer.music.play(-1, 0.0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill(BLACK)
    display_surface.blit(SCORE, score_rect)
    display_surface.blit(TRACKS_SCORE, SCORE)
    display_surface.blit(lives_text, lives_rect)



pygame.display.update()
clock.tick(FPS)


pygame.quit()