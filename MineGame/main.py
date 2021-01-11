import pygame
from setting import *
import time
import random
from datetime import datetime

pygame.init()


# Размер окна
window = pygame.display.set_mode((data["window_w"], data["window_h"]))

# Название игры
pygame.display.set_caption("Car Game")

# Импортируем картинки
carImage = pygame.image.load("assets/car.png")
enemyImage = pygame.image.load("assets/enemy.png")
grass = pygame.image.load("assets/grass.jpg")
yellow_strip = pygame.image.load("assets/yellow_strip.jpg")
strip = pygame.image.load("assets/strip.jpg")

# Время для цикла (Наш цикл будет выполняться каждую секунду)
clock = pygame.time.Clock()

# Здесь рисуем в окне
# Вынесли чтобы все не писать в одном месте
def drawWindow():
    window.fill(GRAY)
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
    pygame.display.update()


# Враг
def enemy(enemyX, enemyY):
    window.blit(enemyImage, (enemyX, enemyY))


# Машина
def car(x, y):
    window.blit(carImage, (x, y))


# один основной цикл
# Пока она равна True цикл наш будет выполняться бесконечно
# как только мы что либо сделаем не так то мы эту переменную сделаем False то сразу выйдем из цикла

# Для текста
def text_objects(text, font):
    textsurface = font.render(text, True, black)
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
    text = font.render("Passed  " + str(passed), True, black)
    score = font.render("Score  " + str(score), True, red)
    window.blit(text, (0, 50))
    window.blit(score, (0, 30))


def game_loop():
    close = False
    x = data["x"]
    y = data["y"]
    y2 = 100
    enemy_speed = data["enemy_speed"]
    enemyX = data["enemyX"]
    enemyY = data["enemyY"]
    enemyX_change = data["enemyX_change"]
    enemyY_change = data["enemyY_change"]
    enemy_width = data["enemy_width"]
    enemy_height = data["enemy_height"]
    passed = 0
    score = 0
    level = 0

    # time for car
    timeforcar = datetime.timestamp(datetime.now()) + 3
    # положение
    direction = True

    while not close:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                close = True

        # х и у координаты для машины
        # keys = pygame.key.get_pressed()

        # if keys[pygame.K_LEFT] and x > 155:
        #     x -= data["left"]

        # if keys[pygame.K_RIGHT] and x < 500 - width - 155:
        #     x += data["right"]

        # передвижение машины
        if timeforcar < datetime.timestamp(datetime.now()):
            timeforcar = datetime.timestamp(datetime.now()) + 1.7
            if direction:
                x -= data["right"]
                direction = False
            else:
                x += data["left"]
                direction = True

        # Задний фон
        drawWindow()

        # Враг
        enemyY -= enemy_speed / 4
        enemy(enemyX, enemyY)
        enemyY += enemy_speed
        if enemyY > window_height:
            enemyY = 0
            passed += 1
            score = passed * 10
            if int(passed) % 5 == 0:
                level += 1
                font = pygame.font.SysFont(None, 100)
                text = font.render("Level  " + str(level), True, black)
                window.blit(text, (100, 200))
                pygame.display.update()
                time.sleep(2)

        window.blit(carImage, (x, y))

        # # # Возвращает размер и местоположение травы get_rect()
        rel_y = y2 % grass.get_rect().width
        window.blit(grass, (0, rel_y - grass.get_rect().width))
        window.blit(grass, (400, rel_y - grass.get_rect().width))
        y2 += speed

        # Для столкновения с врагом
        if y < enemyY:
            if (
                x > enemyX
                and x < enemyX + enemy_width
                or x + car_width > enemyX
                and x + car_width < enemyX + +enemy_width
            ):
                crash()
        score_system(passed, score)
        pygame.display.update()
        clock.tick(10)


game_loop()
pygame.quit()
quit()
