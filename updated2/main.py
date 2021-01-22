import pygame
from setting import *
import time
import random
from datetime import datetime
from enemy import EnemyClass
pygame.init()
frame_per_second = 10
pygame.time.set_timer(pygame.USEREVENT, 2000)


window = pygame.display.set_mode((data["window_width"], data["window_height"]))
pygame.display.set_caption("Car Game")
car_image = pygame.image.load("assets/car.png")
grass = pygame.image.load("assets/grass.jpg")
yellow_strip = pygame.image.load("assets/yellow_strip.jpg")
strip = pygame.image.load("assets/strip.jpg")
clock = pygame.time.Clock()
enemy_images =['enemy.png', 'enemy_2.png']
enemy_in_background = [pygame.image.load('assets/'+path).convert_alpha() for path in enemy_images]

def draw_background():
    window.fill(background_color_gray)
    window.blit(grass, (0, 0))
    window.blit(grass, (400, 0))
    window.blit(yellow_strip, (230, 0))
    window.blit(yellow_strip, (230, 100))
    window.blit(yellow_strip, (230, 200))
    window.blit(yellow_strip, (230, 300))
    window.blit(yellow_strip, (230, 400))
    window.blit(yellow_strip, (230, 500))
    window.blit(yellow_strip, (230, 600))
    window.blit(yellow_strip, (230, 700))
    window.blit(yellow_strip, (230, 800))
    window.blit(yellow_strip, (230, 900))
    window.blit(strip, (150, 0))
    window.blit(strip, (350, 0))

def text_objects(text, font):
    textsurface = font.render(text, True, scoreboard_color_black)
    return textsurface, textsurface.get_rect()

def message_display(text):
    largetext = pygame.font.Font("freesansbold.ttf", 30)
    textsurf, textrect = text_objects(text, largetext)
    textrect.center = ((window_width / 2), (window_height / 2))
    window.blit(textsurf, textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()

def crash():
    message_display("Opps, try again")


def score_system(passed, score):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Passed  " + str(passed), True, scoreboard_color_black)
    score = font.render("Score  " + str(score), True, scoreboard_color_red)
    window.blit(text, (0, 50))
    window.blit(score, (0, 30))


def create_enemy(group):
    enemy_x = 320
    indx = randint(0, len(enemy_in_background)-1)
    speed = randint(1,4)
    return EnemyClass(enemy_x,enemy_speed, enemy_in_background[indx], group)
enemy = pygame.sprite.Group()
create_enemy(enemy)

# def enemy_crash(enemy_y):
#     enemy_y -= enemy_speed / 4
#     enemy_y += enemy_speed
#     if car_y < enemy_y:
#             if (
#                 car_x > enemy_x
#                 and car_x < enemy_x + enemy_width
#                 or car_x + car_width > enemy_y
#                 and car_x + car_width < enemy_x + enemy_width
#             ):
#                 crash()
# Машина
def car(car_x, car_y):
    window.blit(car_image, (car_x, car_y))

def game_loop():
    close = False
    y2=100
    enemy_y = data['enemy_y']
    while not close:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                close = True
            elif event.type == pygame.USEREVENT:
                create_enemy(enemy)
        enemy_crash(enemy_y)
        window.blit(car_image, (car_x, car_y))
        enemy.draw(window)
        clock.tick(frame_per_second)
        enemy.update(window_height)
        rel_y = y2 % grass.get_rect().width
        window.blit(grass, (0, rel_y - grass.get_rect().width))
        window.blit(grass, (400, rel_y - grass.get_rect().width))
        y2 += car_speed
        score_system(passed=0, score=0)
        pygame.display.update()

        
game_loop()
pygame.quit()
quit()
