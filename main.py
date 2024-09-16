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

GREEN = (0, 255, 0)
DARK_GREEN = (10, 50, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FONT = pygame.font.Font('AttackGraffiti.ttf', 32)

TRACKS_SCORE = FONT.render("Score: " + str(SCORE), True, GREEN, DARK_GREEN)
int.Get_Rect()
SCORE.topleft = (10, 10)
game_over_text = "GAMEOVER"
Background = DARK_GREEN

color = GREEN
BACKGROUND = DARK_GREEN
Center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #HERE
    display_surface.fill(BLACK)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(score_text, SCORE_RECT)
    display_surface.blit(lives_text, lives_rect)




pygame.quit()


