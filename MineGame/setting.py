import json
import random
from random import randint
import time
from datetime import datetime


f = open("/home/gulim/CarGames/MineGame/json/car.json")
data = json.load(f)
print(data)

# Цвет заднего фона
GRAY = (119, 118, 110)

# width и height х и у координаты для машины
width = data["width"]
height = data["height"]
window_height = data["window_h"]
window_width = data["window_w"]
x = data["x"]
y = data["y"]
left = data["left"]
right = data["right"]
speed = data["speed"]
speed1 = data["speed_1"]
y2 = 100
left = False
right = False
car_width = 56
# Для показа сообщения
black = (0, 0, 0)
red = (255, 0, 0)
