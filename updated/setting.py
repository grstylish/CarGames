import json
import random
from random import randint
import time
from datetime import datetime
import pygame


json_file = open("/home/gulim/Downloads/CarGame/MineGame/json/car.json")
data = json.load(json_file)
print(data)

background_color_gray = (119, 118, 110)

car_width = data["car_width"]
car_height = data["car_height"]
window_height = data["window_height"]
window_width = data["window_width"]
car_x = data["car_x"]
car_y = data["car_y"]
turn_left = data["turn_left"]
turn_right = data["turn_right"]
car_speed = data["car_speed"]
car_speed1 = data["car_speed_1"]
enemy_x = data['enemy_x']
enemy_y = data['enemy_y']
enemy_speed = data['enemy_speed']
y2 = 100
scoreboard_color_black = (0, 0, 0)
scoreboard_color_red = (255, 0, 0)
