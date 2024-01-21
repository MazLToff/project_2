import pygame
import sys
import random

width = 1200
height = 600
game_images = {}
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


def createPipe():
    offset = height / 3
    pipeHeight = game_images['pipeimage'][0].get_height()
    y2 = offset + \
         random.randrange(
             0, int(height - game_images['sea_level'].get_height() - 1.2 * offset))
    pipeX = width + 10
    y1 = pipeHeight - y2 + offset
    pipe = [
        # upper Pipe
        {'x': pipeX, 'y': -y1},

        # lower Pipe
        {'x': pipeX, 'y': y2}
    ]
    return pipe

def create_post():
    if len(all_posts) == 0 or width - all_posts[-1][1] > 300:
        gm = 200
        post_height = random.randint(50, height - gm - 50)
        post1 = pygame.transform.scale(post_image, (100, post_height))
        post2 = pygame.transform.scale(post_image, (100, height - post_height - gm))

        all_posts.append([post1, width, 0])
        all_posts.append([post2, width, post_height + gm])



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
