import pyglet
from resources import floor, walls_bot, walls_left, all_floor
from pyglet.sprite import Sprite
from window import sprites_per_window_x, sprites_per_window_y
from constants import WINDOW_WIDTH, WINDOW_HEIGHT


FLOOR_BATCH = pyglet.graphics.Batch()

def create_floor():
    if (WINDOW_WIDTH - floor.width // 2) / floor.width != int() or (WINDOW_HEIGHT - floor.height // 2) / floor.height != int():
        tolerance = 1
    else:
        tolerance = 0
    x = sprites_per_window_x(floor)
    y = sprites_per_window_y(floor)
    for y in range(int(sprites_per_window_y(floor) + tolerance)):
        for x in range(int(sprites_per_window_x(floor) + tolerance)):
            all_floor.append(Sprite(img=floor, x = x * floor.width + floor.width // 2 + walls_left[0].width, 
                                    y = y * floor.height + floor.height // 2 + walls_bot[0].height, batch=FLOOR_BATCH))
