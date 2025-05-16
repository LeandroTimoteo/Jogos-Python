

import pygame

# Inicializa o pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Configuração das raquetes e bola
paddle_width, paddle_height = 15, 100
ball_radius = 10
player_speed = 7
ball_speed_x, ball_speed_y = 5, 5

# Posições iniciais
player1 = pygame.Rect(50, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
player2 = pygame.Rect(WIDTH - 65, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, ball_radius, ball_radius)

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)

    # Eventos do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controles dos jogadores
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= player_speed
    if keys[pygame.K_s] and player1.bottom < HEIGHT:
        player1.y += player_speed
    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= player_speed
    if keys[pygame.K_DOWN] and player2.bottom < HEIGHT:
        player2.y += player_speedsw

    # Movimento da bola
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Colisão com as bordas
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Colisão com as raquetes
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1

    # Reiniciar bola se passar das extremidades
    if ball.left <= 0 or ball.right >= WIDTH:
        ball.x, ball.y = WIDTH // 2, HEIGHT // 2

    # Desenhar elementos
    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.line(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

# Please organize the codes //


