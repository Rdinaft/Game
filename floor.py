import pyglet
from resources import floor, walls_bot, walls_left
from pyglet.sprite import Sprite
from window import sprites_per_window_x, sprites_per_window_y
from constants import WINDOW_WIDTH, WINDOW_HEIGHT


FLOOR_BATCH = pyglet.graphics.Batch()
all_floor = []

def create_floor():
    if float((WINDOW_WIDTH - floor.width // 2) / floor.width).is_integer() or float((WINDOW_HEIGHT - floor.height // 2) / floor.height).is_integer():
        tolerance = 1
    else:
        tolerance = 0
    
    for y in range(int(sprites_per_window_y(floor) + tolerance)):
        for x in range(int(sprites_per_window_x(floor) + tolerance)):
            all_floor.append(Sprite(img=floor, x = x * floor.width + floor.width // 2 + walls_left[0].width, 
                                    y = y * floor.height + floor.height // 2 + walls_bot[0].height, batch=FLOOR_BATCH))
