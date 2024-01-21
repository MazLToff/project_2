import pygame
import random

pygame.init()
pygame.font.init()

width = 1200
height = 600
game_images = {}
window = pygame.display.set_mode((width, height))

background_image = pygame.image.load('images/background.png')
background_image = pygame.transform.scale(background_image, (width, height))

hero_image = pygame.image.load('images/hero.png')
hero_image = pygame.transform.scale(hero_image, (80, 45))
hero_x, hero_y = abs(width / 12), abs(height / 2) - 20

post_image = pygame.image.load('images/post.png')
all_posts = []

gravity = 0.006
jump_force = -0.5
hero_velocity = 0
jumping = False
game_over = False

def draw_hero():
    window.blit(hero_image, (hero_x, hero_y))

def create_pipe():
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
    if all_posts and all_posts[0][1] < -100:
        create_pipe()


def collision_check():
    global game_over
    for post in all_posts:
        if hero_x + hero_image.get_width() > post[1] and hero_x < post[1] + post[0].get_width():
            if hero_y < post[2] + post[0].get_height() or hero_y + hero_image.get_height() > post[2] + post[0].get_height() + 200:
                game_over = True

def game_over_screen():
    window.fill((0, 0, 0))

    font = pygame.font.Font(None, 36)
    text = font.render("ИГРА ОКОНЧЕНА", True, (255, 255, 255))
    text_rect = text.get_rect(center=(width/2, height / 2))
    window.blit(text, text_rect)

    pygame.display.flip()


create_pipe()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jumping = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                jumping = False

    if jumping:
        hero_velocity = jump_force
    else:
        hero_velocity += gravity

    hero_y += hero_velocity

    hero_y += hero_velocity

    if hero_y > height:
        hero_y = height

    if hero_y < 0:
        hero_y = 0
    elif hero_y > height - hero_image.get_height():
        hero_y = height - hero_image.get_height()

    collision_check()

    if game_over:
        game_over_screen()
        running = False

    window.blit(background_image, (0, 0))
    draw_hero()
    draw_posts()
    pygame.display.flip()

pygame.quit()
