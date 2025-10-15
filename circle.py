import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Simple Game")
clock = pygame.time.Clock()

player_x, player_y = 200, 150
speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= speed
    if keys[pygame.K_RIGHT]:
        player_x += speed
    if keys[pygame.K_UP]:
        player_y -= speed
    if keys[pygame.K_DOWN]:
        player_y += speed

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (player_x, player_y), 20)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
