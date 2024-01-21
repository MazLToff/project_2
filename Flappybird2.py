import pygame
import pygame.time
import sys
import random

width = 1200
height = 600
window = pygame.display.set_mode((width, height))

background_image = pygame.image.load('images/background.png')
background_image = pygame.transform.scale(background_image, (width, height))

hero_image = pygame.image.load('images/hero.png')
hero_image = pygame.transform.scale(hero_image, (80, 45))
hero_x, hero_y = abs(width / 12), abs(height / 2) - 20,


def draw_hero():
    window.blit(hero_image, (hero_x, hero_y))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                hero_y -= 40
            if event.key == pygame.K_w:
                hero_y -= 40
            if event.key == pygame.K_SPACE:
                hero_y -= 40
    hero_y += 0.1
    if hero_y > height:
        running = False
    window.blit(background_image, (0, 0))
    draw_hero()
    pygame.display.flip()

pygame.quit()
