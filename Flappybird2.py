import pygame
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

post_image = pygame.image.load('images/post.png')
all_posts = []


def draw_hero():
    window.blit(hero_image, (hero_x, hero_y))


def create_post():
    post1, post2 = post_image, post_image

    post1_height = random.randint(100, 400)
    post1 = pygame.transform.scale(post1, (100, post1_height))
    post2 = pygame.transform.scale(post2, (100, (600 - post1_height) - 100))

    all_posts.append([post1, 1200, 0])
    all_posts.append([post2, 1200, 500])


def draw_posts():
    for post in all_posts:
        window.blit(post[0], (post[1], post[2]))
        post[1] -= 0.7
    if post[1] < 600:
        create_post()


create_post()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                hero_y -= 50
            if event.key == pygame.K_w:
                hero_y -= 50
            if event.key == pygame.K_SPACE:
                hero_y -= 50
    hero_y += 0.3
    if hero_y > height:
        running = False
    window.blit(background_image, (0, 0))
    draw_hero()
    draw_posts()
    pygame.display.flip()

pygame.quit()
