import pyglet
import random
from pyglet.sprite import Sprite
from resources import walls_top, walls_left, walls_right, walls_bot
from window import WINDOW, sprites_per_window_x, sprites_per_window_y


WALL_BATCH = pyglet.graphics.Batch()

def create_walls(walls):
    vert_wall = walls_left[0]
    horiz_wall = walls_top[0]
    for x in range(int(sprites_per_window_x(horiz_wall))):
        top_walls = Sprite(random.choice(walls_top), x = x * horiz_wall.width + vert_wall.width, y = WINDOW.height - horiz_wall.height, batch = WALL_BATCH)
        bot_walls = Sprite(random.choice(walls_bot), x = x * horiz_wall.width + vert_wall.width, y = 0, batch = WALL_BATCH)
        walls += top_walls, bot_walls
    for y in range(int(sprites_per_window_y(vert_wall))):
        left_walls = Sprite(random.choice(walls_left), x = 0, y = y * vert_wall.height, batch = WALL_BATCH)
        right_walls = Sprite(random.choice(walls_right), x = WINDOW.width - vert_wall.width, y = y * vert_wall.height, batch = WALL_BATCH)
        walls += left_walls, right_walls
