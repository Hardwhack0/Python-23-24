import pygame
import sys

# Inicializace Pygame
pygame.init()

# Velikost okna
width = 800
height = 600

# Barvy
white = (255, 255, 255)
black = (0, 0, 0)

# Vlastnosti hráčů
player_width = 15
player_height = 90
player_speed = 10

# Vlastnosti míčku
ball_size = 20
ball_speed_x = 7
ball_speed_y = 7

# Inicializace hráčů a míčku
player1_pos = pygame.Rect(50, height / 2 - player_height / 2, player_width, player_height)
player2_pos = pygame.Rect(width - 50 - player_width, height / 2 - player_height / 2, player_width, player_height)
ball_pos = pygame.Rect(width / 2 - ball_size / 2, height / 2 - ball_size / 2, ball_size, ball_size)

# Vytvoření okna
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

# Hlavní smyčka programu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Pohyb hráčů
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1_pos.y -= player_speed
    if keys[pygame.K_s]:
        player1_pos.y += player_speed
    if keys[pygame.K_UP]:
        player2_pos.y -= player_speed
    if keys[pygame.K_DOWN]:
        player2_pos.y += player_speed

    # Omezení pohybu hráčů na hranice okna
    player1_pos.y = max(0, min(height - player_height, player1_pos.y))
    player2_pos.y = max(0, min(height - player_height, player2_pos.y))

    # Pohyb míčku
    ball_pos.x += ball_speed_x
    ball_pos.y += ball_speed_y

    # Kolize míčku s hranami pole
    if ball_pos.top <= 0 or ball_pos.bottom >= height:
        ball_speed_y = -ball_speed_y
    if ball_pos.left <= 0 or ball_pos.right >= width:
        ball_speed_x = -ball_speed_x

    # Kolize míčku s hráči
    if ball_pos.colliderect(player1_pos) or ball_pos.colliderect(player2_pos):
        ball_speed_x = -ball_speed_x

    # Vykreslení
    screen.fill(black)
    pygame.draw.rect(screen, white, player1_pos)
    pygame.draw.rect(screen, white, player2_pos)
    pygame.draw.ellipse(screen, white, ball_pos)
    pygame.display.flip()

    # Zpoždění pro plynulý pohyb
    pygame.time.Clock().tick(60)

# Ukončení Pygame
pygame.quit()
sys.exit()