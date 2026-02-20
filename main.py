import pygame
from sys import exit


GAME_WIDTH = 360
GAME_HEIGHT = 780

pygame.init()
window = pygame.display.set_mode((GAME_WIDTH , GAME_HEIGHT))
pygame.display.set_caption("Will i ever get a job? - No")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    pygame.display.update()
    clock.tick(30) #30 fps