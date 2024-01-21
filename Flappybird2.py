import pygame
import sys
import random

width = 1000
height = 600
window = pygame.display.set_mode((width, height))

background_image = pygame.image.load('images/background.png')
background_image = pygame.transform.scale(background_image, (width, height))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.blit(background_image, (0, 0))
    pygame.display.flip()

pygame.quit()
